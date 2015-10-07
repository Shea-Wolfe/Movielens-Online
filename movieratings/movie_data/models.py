from django.db import models

# Create your models here.
class Rater(models.Model):
    male = 'm'
    female = 'f'
    gender_choices = [(male,'Male'),(female,'Female')]
    gender = models.CharField(max_length=1,choices=gender_choices,default=male)
    zip_code = models.CharField(max_length=5)
    age = models.PositiveSmallIntegerField()
    occupation = models.CharField(max_length=255)

    def __str__(self):
        return 'user #{}'.format(self.id)


class Movie(models.Model):
    title = models.CharField(max_length=255)

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

def import_users():
    import csv
    import json

    users = []

    with open('ml-1m/users.dat') as f:

        reader= csv.DictReader([line.replace('::','\t') for line in f],
                                fieldnames='UserID::Gender::Age::Occupation::Zip-code'.split('::'),
                                delimiter='\t')
        for row in reader:
            user = {'fields': {'gender':row['Gender'],
                                'age':row['Age'],
                                'occupation':row['Occupation'],
                                'zip-code':row['Zip-code']},
                    'model':'movie_data.Rater',
                    'pk':int(row['UserID'])
            }
            users.append(user)

    with open('users.json','w') as f:
        f.write(json.dumps(users))
