# Description:

* This is a Django project to look at the movielens data
* Currently contains one app called movie_data
* movie_data has three models; raters, ratings, and movies.
* movie_data has admin registered so that all three models can be clearly interacted with.

## Building the Database:

* In order to view the data you will need to get the movielens 1 million data from http://grouplens.org/datasets/movielens/ and unzip it into a directory named ml-1m which is in movieratings (at the same depth as manage.py)
* Run python manage.py makemigrations
* Run python manage.py migrate to setup the database
* Once you've done that from the directory containing manage.py open the shell and run "from movie_data import \*" <strong>This MUST be done while you are in the same directory as manage.py</strong>
* Then run "models.import_all_data()" This will load the data into your database.  It will take a few minutes.
* Once the data is in and you have the server running the path to the three views are:
  1. localhost:8000/u/movie/1 (can be any number corresponds with movie id) which gets the movies page.
  1. localhost:8000/u/moive/top which gets the top 20 rated movies. Loads slowly.
  1. localhost:8000/u/user/1 (can be any number: corresponds with user id) which gets that users page.
