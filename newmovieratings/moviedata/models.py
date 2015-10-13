from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
# Create your models here.

class Rater(models.Model):
    zipcode = models.CharField(max_length=10)
    male = 'm'
    female = 'f'
    gender_choices = [(male,'Male'),(female,'Female')]
    gender = models.CharField(choices=gender_choices,max_length=1)
    age = models.PositiveSmallIntegerField(validators=[RegexValidator(r'(\d{1:2}|100)$',message='Please enter an age between 1 and 100')])
    occupation = models.CharField(max_length=255,validators=[RegexValidator(r'\d+$',message='Please enter your occupation\'s code number')])
    user = models.OneToOneField(User,null=True)

    # def movies_rated(self):
    #     return [Rating.movie for rating in self.rating_set.all()]



class Movie(models.Model):
    title = models.CharField(max_length=255)

    def average_rating(self):
        return self.rating_set.all().aggregate(models.Avg('score'))['score__avg']



    def __str__(self):
        return self.title


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    score = models.PositiveSmallIntegerField(choices = [(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')])
    timestamp = models.DateTimeField(null=True)
    review = models.TextField(max_length=400,null=True, blank=True)
