
# from django.urls import path
# from . import views

# app_name = 'myApp'

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('upload_photo/', views.PhotoUploadView.as_view(), name='upload_photo'),
#     path('upload_portrait/', views.PortraitUploadView.as_view(), name='upload_portrait'),
#     path('upload_artwork/', views.ArtworkUploadView.as_view(), name='upload_artwork'),
#     path('detail/<int:pk>/', views.ArtworkDetailView.as_view(), name='artwork_detail'),
#     path('portrait/<int:pk>/', views.PortraitDetailView.as_view(), name='portrait_detail'),
#     path('artwork/<int:pk>/', views.ArtworkDetailView.as_view(), name='artwork_detail'),
# ]

from django.urls import path
from . import views

app_name = 'myApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('upload_photo/', views.PhotoUploadView.as_view(), name='upload_photo'),
    path('upload_portrait/', views.PortraitUploadView.as_view(), name='upload_portrait'),
    path('upload_artwork/', views.ArtworkUploadView.as_view(), name='upload_artwork'),
    path('detail/<int:pk>/', views.ArtworkDetailView.as_view(), name='artwork_detail'),
    path('portrait/<int:pk>/', views.PortraitDetailView.as_view(), name='portrait_detail'),
    path('artwork/<int:pk>/', views.ArtworkDetailView.as_view(), name='artwork_detail'),
    path('search_form/', views.search_form, name='search_form'),
    path('view_my_photos/', views.view_my_Photos, name='view_my_photos'),
    path('view_my_potraits/', views.view_my_potraits, name='view_my_potraits'),
    path('view_my_artworks/', views.view_my_artworks, name='view_my_artworks'),
]
