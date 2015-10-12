# Description:

* This is a Django project to look at the movielens data
* Currently contains two apps movie_data and users
* movie_data has three models; raters, ratings, and movies. Users has one, Users

## Building the Database:

* In order to view the data you will need to get the movielens 1 million data from http://grouplens.org/datasets/movielens/ and unzip it into a directory named ml-1m which is in movieratings (at the same depth as manage.py)
* Run python manage.py makemigrations
* Run python manage.py migrate to setup the database
* Once you've done that from the directory containing manage.py open the shell and run "from moviedata.models import \*" <strong>This MUST be done while you are in the same directory as manage.py</strong>
* Then run "get_all_data()" This will create JSON files for all the data.  It will take a few moments.
* finally exit out of the shell and run these three commands
  * $ python manage.py loaddata moviedata/fixtures/ratings.json.
  * $ python manage.py loaddata moviedata/fixtures/raters.json.
  * $ python manage.py loaddata moviedata/fixtures/movies.json.

## Using the apps

* First run $ python manage.py runserver. to start the server running.
* Once the server is running open a browser and go to localhost:8000/login to begin
* If you don't want to register, you can enter localhost:8000/u/rater/1 to get started, but there is a loss of functionality.
* If you want to try playing around as another (fake) user first enter the shell.  Next enter from moviedata.models import \*. Then type Rater.objects.all().first().user to get a username.  Their passwords are all 'password'.
