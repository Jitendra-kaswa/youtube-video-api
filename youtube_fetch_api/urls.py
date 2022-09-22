"""youtube_fetch_api URL Configuration

Here i have added two urls , one for admin and another for youtube API calls, since i am using class view,
so i don't need to add a diferent url for each type of call. 

"""
from django.contrib import admin
from django.urls import path

from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.YoutubeVideoView.as_view())
]
