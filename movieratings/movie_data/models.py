from django.db import models
from django.contrib.auth.models import User
from faker import Faker
fake = Faker()
# Create your models here.
class Rater(models.Model):
    male = 'm'
    female = 'f'
    gender_choices = [(male,'Male'),(female,'Female')]
    gender = models.CharField(max_length=1,choices=gender_choices,default=male)
    zip_code = models.CharField(max_length=5)
    age = models.PositiveSmallIntegerField()
    occupation = models.CharField(max_length=255)
    user = models.OneToOneField(User, null=True)


    def __str__(self):
        return 'user #{}'.format(self.id)

    def generate_user(self):
        self.user = User.objects.create_user(fake.user_name(), password='password', email=fake.email())
        self.save()

class Movie(models.Model):
    title = models.CharField(max_length=255)

    def average_rating(self):
        return self.rating_set.aggregate(models.Avg('score'))['score__avg']

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
                                'zip_code':row['Zip-code']},
                    'model':'movie_data.Rater',
                    'pk':int(row['UserID'])
            }
            users.append(user)

    with open('./movie_data/fixtures/users.json','w') as f:
        f.write(json.dumps(users))

def import_movies():
    import csv
    import json

    movies = []

    with open('ml-1m/movies.dat',encoding='windows-1252') as f:
        reader = csv.DictReader([line.replace('::','\t') for line in f],
                                fieldnames=['MovieID','MovieTitle'],
                                delimiter='\t',
                                )
        for row in reader:
            movie = {'fields': {'title':row['MovieTitle']},
                    'model':'movie_data.Movie',
                    'pk':int(row['MovieID']),
            }
            movies.append(movie)

    with open('./movie_data/fixtures/movies.json','w') as f:
        f.write(json.dumps(movies))

def import_ratings():
    import csv
    import json

    ratings = []

    with open('ml-1m/ratings.dat') as f:
        reader = csv.DictReader([line.replace('::','\t') for line in f],
                                fieldnames=['UserID','MovieID','Score'],
                                delimiter='\t'
                                )
        for row in reader:
            rating = {'fields': {'movie':row['MovieID'],
                                'rater':row['UserID'],
                                'score':row['Score']},
                      'model': 'movie_data.Rating',
            }

            ratings.append(rating)

    with open('./movie_data/fixtures/ratings.json','w') as f:
        f.write(json.dumps(ratings))

def import_all_data():
    import_users()
    import_movies()
    import_ratings()



def generate_all_users():
    username_set = {fake.user_name() for _ in range(9000)}
    username_list = [x for x in username_set]
    count = 0
    for rater in Rater.objects.all():
        if rater.user == None:
            rater.user = User.objects.create_user(username_list[count],password='password',email=fake.email())
            rater.save()
        count += 1
