from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from app.views import SampleClass
from app.views import (HeadlineDetailView, HeadlineListView)
from django.urls import path
from login import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^$', SampleClass.as_view(), name='home'),
  #path('', views.indexView, name="home"),
  url(r'^headlines/$', HeadlineListView.as_view(), name='headlines'),

  url(r'^headlines/(?P<slug>[\w-]+)/$', HeadlineDetailView.as_view()),
  path('dashboard/', views.dashboardView, name="dashboard"),
  path('login/', LoginView.as_view(), name="login_url"),
  path('register/', views.registerView, name="register_url"),
  path('logout/', LogoutView.as_view(next_page="login_url"), name="logout"),
]

