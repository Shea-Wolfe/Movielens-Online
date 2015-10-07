from django.db import models

# Create your models here.
class Rater(models.Model):
    gender = models.CharField(max_length=1)

class Movie(models.Model):
    title = models.CharField(max_length=25)

class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    score = models.IntegerField()
