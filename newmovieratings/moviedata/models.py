from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Rater(models.Model):
    zipcode = models.CharField(max_length=5)
    male = 'm'
    female = 'f'
    gender_choices = [(male,'Male'),(female,'Female')]
    gender = models.CharField(choices=gender_choices,max_length=1)
    age = models.PositiveSmallIntegerField()
    occupation = models.CharField(max_length=255)
    user = models.OneToOneField(User,null=True)


class Movie(models.Model):
    title = models.CharField(max_length=255)

class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    score = models.PositiveSmallIntegerField(choices = [(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5')])

def generate_users():
    from faker import Faker
    fake = Faker()
    user_list = [x for x in {fake.user_name() for _ in range(9000)}]
    count = 0
    for rater in Rater.objects.all():
        if rater.user == None:
            rater.user = User.objects.create_user(user_list[count],password='password',email=fake.email())
            rater.save()
        count += 1



def get_raters():
    import csv
    import json
    raters = []
    with open('ml-1m/users.dat') as f:
        reader = csv.DictReader([line.replace('::','\t') for line in f],
                                fieldnames=['userid','gender','age','occupation','zip'],
                                delimiter='\t')
        for row in reader:
            rater = {'fields':{'gender':row['gender'],
                                'age':row['age'],
                                'occupation':row['occupation'],
                                'zipcode': row['zip']},
                    'model':'moviedata.Rater',
                    'pk':row['userid']}
            raters.append(rater)
    with open('./moviedata/fixtures/raters.json','w') as f:
        f.write(json.dumps(raters))

def get_movies():
    import csv
    import json
    movies = []
    with open('ml-1m/movies.dat', encoding='Windows-1252') as f:
        reader = csv.DictReader([line.replace('::','\t') for line in f],
                                fieldnames=['movieid','title'],
                                delimiter='\t')
        for row in reader:
            movie = {'fields':{'title':row['title']},
                    'model':'moviedata.Movie',
                    'pk':row['movieid']}
            movies.append(movie)
    with open('./moviedata/fixtures/movies.json','w') as f:
        f.write(json.dumps(movies))

def get_ratings():
    import csv
    import json
    ratings = []
    with open('ml-1m/ratings.dat') as f:
        reader = csv.DictReader([line.replace('::','\t') for line in f],
                                fieldnames=['userid','movieid','score'],
                                delimiter='\t')
        for row in reader:
            rating = {'fields':{'rater':row['userid'],
                                'movie':row['movieid'],
                                'score':row['score'],
                                },
                    'model':'moviedata.Rating',}
            ratings.append(rating)
    with open('./moviedata/fixtures/ratings.json','w') as f:
        f.write(json.dumps(ratings))

def get_all_data():
    get_raters()
    get_movies()
    get_ratings()
