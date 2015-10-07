from django.contrib import admin
from .models import Movie,Rating,Rater


class MovieAdmin(admin.ModelAdmin):
    list_display = ['id','title']


class RatingAdmin(admin.ModelAdmin):
    list_display = ['rater','movie','score']


class RatingRater(admin.ModelAdmin):
    list_display = ['id', 'gender']


# Register your models here.
admin.site.register(Movie,MovieAdmin)
admin.site.register(Rating,RatingAdmin)
admin.site.register(Rater,RatingRater)
