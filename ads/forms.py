from django import forms
from .models import Ads


class AdForm(forms.Form):
    title = forms.CharField(max_length=150)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.FloatField()
    image = forms.ImageField()
    type = forms.ChoiceField(choices=Ads.TYPE_OF_ADS)
    subcategory = forms.IntegerField()
    owner = forms.IntegerField()
    