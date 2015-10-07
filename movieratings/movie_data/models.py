from django.db import models

# Create your models here.
class Rater(models.Model):
    male = 'm'
    female = 'f'
    gender_choices = [(male,'Male'),(female,'Female')]
    gender = models.CharField(max_length=1,choices=gender_choices,default=male)

    def __str__(self):
        return 'user #{}'.format(self.id)


class Movie(models.Model):
    title = models.CharField(max_length=25)

    def average_rating(self):
        return self.ratings_set.aggrigrate(models.Avg('score'))['score__avg']

    def __str__(self):
        return 'Movie #{}, {}'.format(self.id,self.title)


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    score = models.PositiveSmallIntegerField()

    def __str__(self):
        return '{} gives {} a {}'.format(self.rater,self.movie,self.score)
