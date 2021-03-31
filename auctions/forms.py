from django import forms

attributes = {
    'class': 'form-control mb-3 mt-0 text-info',
    'rows': 3
}

# choices list copied from ebay
categories = (('Antiques', 'Antiques'),
('Art', 'Art'),
('Baby', 'Baby'),
('Books', 'Books'),
('Business & Industrial', 'Business & Industrial'),
('Cameras & Photo', 'Cameras & Photo'),
('Cell Phones & Accessories', 'Cell Phones &  Accessories'),
('Clothing, Shoes & Accessories', 'Clothing, Shoes & Accessories'),
('Coins & Paper Money', 'Coins & Paper Money'),
('Collectibles', 'Collectibles'),
('Computers or Tablets & Networking', 'Computers/Tablets & Networking'),
('Consumer Electronics', 'Consumer Electronics'),
('Crafts', 'Crafts'),
('Dolls & Bears', 'Dolls & Bears'),
('DVDs & Movies', 'DVDs & Movies'),
('eBay Motors', 'eBay Motors'),
('Entertainment Memorabilia', 'Entertainment Memorabilia'),
('Gift Cards & Coupons', 'Gift Cards & Coupons'),
('Health & Beauty', 'Health & Beauty'),
('Home & Garden', 'Home & Garden'),
('Jewelry& Watches', 'Jewelry & Watches'),
('Music', 'Music'),
('Musical Instruments & Gear', 'Musical Instruments & Gear'),
('Pet Supplies', 'Pet Supplies'),
('Pottery & Glass', 'Pottery & Glass'),
('Real Estate', 'Real Estate'),
('Specialty Services', 'Specialty Services'),
('Sporting Goods', 'Sporting Goods'),
('Sports Mem, Cards& Fan Shop', 'Sports Mem, Cards & Fan Shop'),
('Stamps', 'Stamps'),
('Tickets & Experiences', 'Tickets & Experiences'),
('Toys & Hobbies', 'Toys & Hobbies'),
('Travel', 'Travel'),
('Video Games & Consoles', 'Video Games& Consoles'),
('Everything Else', 'Everything Else'),)


class NewListingForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100, widget=forms.TextInput(attrs=attributes))
    description = forms.CharField(max_length=200, widget=forms.Textarea(attrs=attributes))
    starting_bid = forms.DecimalField(widget=forms.NumberInput(attrs=attributes))
    photo_url = forms.CharField(required=False, label='(Optional) Photo URL', max_length=200, widget=forms.TextInput(attrs=attributes))
    category = forms.CharField(widget=forms.Select(choices=categories))
    category.widget.attrs.update(attributes)
