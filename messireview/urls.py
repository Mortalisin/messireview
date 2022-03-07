from django.contrib import admin
from django.urls import path
from messireview import views


urlpatterns = [
    path("", views.index,name='messireview'),
    path("about", views.about,name='about'),
    path("services", views.services,name='services'),
    path("contact", views.contact,name='contact'),
    path("rating",views.rating,name='rating')

]
