from django import forms
from .models import Photo, Portrait, Artwork

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'description', 'image']

class PortraitForm(forms.ModelForm):
    class Meta:
        model = Portrait
        fields = ['title', 'description', 'image']

class ArtworkForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = ['title', 'description', 'image']
