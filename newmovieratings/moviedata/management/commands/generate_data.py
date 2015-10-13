from django.core.management.base import BaseCommand
from moviedata.models import Rater,Rating,Movie
from django.contrib.auth.models import User
from faker import Faker
from datetime import datetime




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
    fake = Faker()
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

class Command(BaseCommand):
    def handle(self, *args, **options):
        get_all_data()
