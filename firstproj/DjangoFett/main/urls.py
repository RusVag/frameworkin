# from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homePage),
    path('news', views.news),
    path('management', views.management),
    path('facts', views.facts),
    path('contacts', views.contacts),
    path('history', views.history),
    path('history/people', views.historyPeople),
    path('history/photos', views.historyPhoto),
    path('news/<text>', views.newsNotFound),
    # path('header', views.header),
    path('facts/<text>', views.factsNotFound),
    path('management/<text>', views.managementNotFound),
    path('contacts/<text>', views.contactsNotFound),
    path('/<text>', views.homeNotFound),
    path('history/<text>', views.historyNotFound),
]
