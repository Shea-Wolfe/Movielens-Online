from django.conf.urls import url
from moviedata.views import Top_20_Rated
urlpatterns = [
    url(r'^movie/(?P<movie_id>\d+)', 'moviedata.views.movie_page', name='movie_page'),
    url(r'^rater/(?P<rater_id>\d+)', 'moviedata.views.rater_page', name='rater_page'),
    url(r'^movie/popular', Top_20_Rated.as_view(),name='popular'),
    url(r'^review_page/(?P<movie_id>\d+)/(?P<rater_id>\d+)', 'moviedata.views.review_page', name='review_page'),
]
