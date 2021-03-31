from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User, Comment, Listing, Bid
from .forms import NewListingForm
from .utils import *

def index(request):
    
    return render(request, "auctions/index.html", {
        "header": "Active Listings:",
        "listings": Listing.objects.filter(winner=None)
    })

def watchlist(request):
    return render(request, "auctions/index.html", {
        "header": "Your watchlist:",
        "listings": request.user.following.all()
    })

def show_all(request):

    return render(request, "auctions/index.html", {
        "header": "All Listings:",
        "listings": Listing.objects.all()
    })

def my_posts(request):
    return render(request, "auctions/index.html", {
        "header": "Your posts:",
        "listings": Listing.objects.filter(owner=request.user).all()
    })


# browse a category
def category(request, category):
    print(f"looking for category {category}")
    return render(request, "auctions/index.html", {
        "header": f"Category - {category}:",
        "listings": Listing.objects.filter(category=category).all()
    })

# creating new listing
def create(request):
    if request.method == "POST":
        form = NewListingForm(request.POST)
        if form.is_valid():
            new_listing = save_listing(request, form)
            new_listing.owner = request.user
            new_listing.save()
            return HttpResponseRedirect(reverse('index'))
        
    return render(request, "auctions/create.html", {
        "form": NewListingForm()
    })



def listing(request, uuid, title):
    user = request.user
    listingobj = Listing.objects.filter(uuid=uuid)[0]
    if request.method == "POST":
        # user placed a bid on this item
        try:
            if request.POST['bid']:
                amount = int(request.POST['bid'])
                bid = Bid(amount=amount, bidder=user)
                Bid.save(bid)
                listingobj.total_price += amount
                listingobj.last_bid = bid
                listingobj.save()
        except:
            pass
    
        # user added/removed from watchlist
        try:
            if request.POST['wl']:
                if user in listingobj.following.all():
                    listingobj.following.remove(user)
                else:
                    listingobj.following.add(user)
        except:
            pass

        # user closed this listing
        try:
            if request.POST['close']:
                if listingobj.last_bid.bidder == user:
                    # no one placed a bid yet
                    return render(request, "auctions/listing.html", {
                        "listing": listingobj,
                        "close_bid_message": "No one placed a bid on your item yet."
                    })
                listingobj.winner = listingobj.last_bid.bidder
                listingobj.save()
                return HttpResponseRedirect(reverse('index'))
        except:
            pass

        # user commented on this listing
        try:
            if request.POST['comment']:
                comment = Comment(author=user, listing=listingobj, text=request.POST['comment'])
                Comment.save(comment)
                listingobj.comments.add(comment)
                listingobj.save()
        except:
            pass

    # return to the same listing
    return render(request, "auctions/listing.html", {
        "listing": listingobj
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
