from django.db import models

# Create your models here.
class Rater(models.Model):
    

class Movie(models.Model):
    title = models.CharField(max_length=25)

class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    score = models.IntegerField(max_length=1)
