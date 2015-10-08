from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^movie/top', views.top_movies),
    url(r'^movie/(?P<movie_id>)\d+', views.show_movie, name='movie_page'),
    url(r'^user/(?P<user_id>\d+)$', views.show_user, name='user_page'),
]
