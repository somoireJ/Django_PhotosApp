from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django_filters.views import FilterView
from .models import Photo, Portrait, Artwork
from .filters import ArtworkFilter
from .forms import PhotoForm, PortraitForm, ArtworkForm



def home(request):
    photos = Photo.objects.all()
    portraits = Portrait.objects.all()
    artworks = Artwork.objects.all()
    artwork_filter = ArtworkFilter(request.GET, queryset=artworks)
    return render(request, 'home.html', {'photos': photos, 'portraits': portraits, 'artworks': artwork_filter.qs, 'filter': artwork_filter})

def search_form(request):
    query = request.GET.get('query')
    photos = Photo.objects.filter(title__icontains=query) | Photo.objects.filter(description__icontains=query)
    return render(request, 'view_my_photos.html', {'photos': photos, 'query': query})


def view_my_Photos(request):
    photos = Photo.objects.all()
    return render(request, 'view_my_photos.html', {'photos': photos})


def view_my_potraits(request):
    portraits = Portrait.objects.all()
    return render(request, 'view_my_potraits.html', { 'portraits': portraits})


def view_my_artworks(request):

    artworks = Artwork.objects.all()
    return render(request, 'view_my_artworks.html', {'artworks': artworks})


class ArtworkDetailView(DetailView):
    model = Artwork
    template_name = 'detail.html'


class PhotoUploadView(CreateView):
    model = Photo
    fields = ['title', 'description', 'image']
    template_name = 'upload_photo.html'
    success_url = reverse_lazy('myApp:home')


class PortraitUploadView(CreateView):
    model = Portrait
    fields = ['title', 'description', 'image']
    template_name = 'upload_portrait.html'
    success_url = reverse_lazy('myApp:home')


class ArtworkUploadView(CreateView):
    model = Artwork
    fields = ['title', 'description', 'image']
    template_name = 'upload_artwork.html'
    success_url = reverse_lazy('myApp:home')


class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'detail.html'


class PortraitDetailView(DetailView):
    model = Portrait
    template_name = 'detail.html'


class ArtworkDetailView(DetailView):
    model = Artwork
    template_name = 'detail.html'

