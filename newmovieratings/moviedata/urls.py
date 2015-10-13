from django.conf.urls import include, url
urlpatterns = [
    url(r'^movie/(?P<movie_id>\d+)', 'moviedata.views.movie_page', name='movie_page'),
    url(r'^rater/(?P<rater_id>\d+)', 'moviedata.views.rater_page', name='rater_page'),
    url(r'^movie/top', 'moviedata.views.top_20',name='top_20'),
]
