from django.conf.urls import include, url
urlpatterns = [
    url(r'^movie/(?P<movie_id>\d+)', 'moviedata.views.movie_page', name='movie_page'),
    url(r'^rater/(?P<rater_id>\d+)', 'moviedata.views.rater_page', name='rater_page'),
    url(r'^movie/top', 'moviedata.views.top_20',name='top_20'),
    url(r'^movie/popular', 'moviedata.views.top_20_rated',name='popular'),
    url(r'^review_page/(?P<movie_id>\d+)/(?P<rater_id>\d+)', 'moviedata.views.review_page', name='review_page'),
]
