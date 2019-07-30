from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from app.views import SampleClass
from app.views import (HeadlineDetailView, HeadlineListView)
from django.urls import path
from login import views
from django.contrib.auth.views import LoginView, LogoutView
#from main.views import scrape
from main import urls

urlpatterns = [
  path('', include('main.urls')),
]

