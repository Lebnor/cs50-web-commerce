from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User, Comment, Listing
from .forms import NewListingForm
from .utils import *

def index(request):
    
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.filter(winner=None)
    })


def create(request):
    if request.method == "POST":
        form = NewListingForm(request.POST)
        if form.is_valid():
            save_listing(form)


            return HttpResponseRedirect(reverse('index'))
        
    return render(request, "auctions/create.html", {
        "form": NewListingForm()
    })



def listing(request, uuid, title):
    user = request.user
    listingobj = Listing.objects.filter(uuid=uuid)[0]

    if request.method == "POST":
        try:
            if request.POST['bid']:
                print(request.POST['bid'])
                listingobj.bid=request.POST['bid']
                listingobj.save()
        
        except:
            pass
        try:
            if request.POST['wl']:
                if user in listingobj.following.all():
                    listingobj.following.remove(user)
                else:
                    listingobj.following.add(user)
        except:
            pass

        

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
