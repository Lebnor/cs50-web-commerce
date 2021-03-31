from .models import Listing, Bid

def save_listing(request, form):
    title = form.cleaned_data['title']
    description = form.cleaned_data['description']
    photo_url = form.cleaned_data['photo_url']
    category = form.cleaned_data['category']
    if not category:
        category = "Everything Else"
    starting_bid = form.cleaned_data['starting_bid']
    bid = Bid(bidder=request.user, amount=starting_bid)
    Bid.save(bid)
    new_listing = Listing(
        title=title,
        description=description,
        last_bid=bid,
        photourl=photo_url,
        category=category
    )

    Listing.save(new_listing)
    return new_listing
