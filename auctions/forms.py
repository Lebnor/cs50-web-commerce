from django import forms

attributes = {
    'class': 'form-control mb-3 mt-0 text-info',
    'rows': 3
}

class NewListingForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100, widget=forms.TextInput(attrs=attributes))
    description = forms.CharField(max_length=200, widget=forms.Textarea(attrs=attributes))
    starting_bid = forms.DecimalField(widget=forms.NumberInput(attrs=attributes))
    photo_url = forms.CharField(required=False, label='(Optional) Photo URL', max_length=200, widget=forms.TextInput(attrs=attributes))
    category = forms.CharField(required=False, label='(Optional) Category', max_length=32, widget=forms.TextInput(attrs=attributes))

