from django import forms

attributes = {
    'class': 'form-control'
}


class NewListingForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100, widget=forms.TextInput(attrs=attributes))
    description = forms.CharField(widget=forms.Textarea(attrs=attributes))
    starting_bid = forms.DecimalField(widget=forms.NumberInput(attrs=attributes))
