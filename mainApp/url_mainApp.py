from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('getImage/', views.getImage, name='getImage'),
    path('canvas/', views.canvas, name='canvas'),
    path('toGray/', views.toGray, name='toGray'),
    path('canvas/brightness/<brightness_type>/', views.brightness, name='brightness'),
    path('negative/', views.negative, name='negative'),
    path('undo/', views.undo_all, name='undo'),
    path('crop/', views.crop, name='crop'),
]