"""newmovieratings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login', 'users.views.user_login', name='login'),
    url(r'^logout','users.views.user_logout',name='logout'),
    url(r'^register','users.views.new_user', name='register'),
    url(r'^new_rating','users.views.rate_movie',name='new_rating'),
    url(r'^user_rating/(?P<movie_id>\d+)','users.views.user_rating',name='user_rating'),
    url(r'^u/', include('moviedata.urls'))
]
