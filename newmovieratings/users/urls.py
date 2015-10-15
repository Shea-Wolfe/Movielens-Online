from django.conf.urls import url

urlpatterns = [
    url(r'^accounts/login', 'users.views.user_login', name='login'),
    url(r'^logout','users.views.user_logout',name='logout'),
    url(r'^register','users.views.new_user', name='register'),
    url(r'^new_rating','users.views.rate_movie',name='new_rating'),
    url(r'^user_rating/(?P<movie_id>\d+)','users.views.user_rating',name='user_rating'),
    url(r'^remove_rating/(?P<movie_id>\d+)', 'users.views.remove_rating', name='remove_rating'),
    url(r'^update_rater', 'users.views.update_rater',name='update_rater'),
]
