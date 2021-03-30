from .models import Listing

def save_listing(form):
    title = form.cleaned_data['title']
    description = form.cleaned_data['description']
    starting_bid = form.cleaned_data['starting_bid']
    photo_url = form.cleaned_data['photo_url']
    category = form.cleaned_data['category']

    new_listing = Listing(
        title=title,
        description=description,
        bid=starting_bid,
        photourl=photo_url,
        category=category
    )

    Listing.save(new_listing)
