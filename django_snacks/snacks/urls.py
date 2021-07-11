from os import name
from django.urls import path
from .views import AboutViews, HomeViews


urlpatterns = [
    path('', HomeViews.as_view(), name='home'),
    path('about', AboutViews.as_view(), name='about')
]
