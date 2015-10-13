# Description:

* This is a Django project to look at the movielens data
* Currently contains two apps movie_data and users
* movie_data has three models; raters, ratings, and movies. Users has one, Users

## Building the Database:

* In order to view the data you will need to get the movielens 1 million data from http://grouplens.org/datasets/movielens/ and unzip it into a directory named ml-1m which is in movieratings (at the same depth as manage.py)
* Run python manage.py makemigrations
* Run python manage.py migrate to setup the database
* Run python manage.py generate_data
* Next run these three commands
  * $ python manage.py loaddata moviedata/fixtures/ratings.json.
  * $ python manage.py loaddata moviedata/fixtures/raters.json.
  * $ python manage.py loaddata moviedata/fixtures/movies.json.
* Once that's done (it will take a while) run python manage.py generate_users

## Using the apps

* First run $ python manage.py runserver. to start the server running.
* Once the server is running open a browser and go to localhost:8000/login to begin
* If you don't want to register, you can enter localhost:8000/u/rater/1 to get started, but there is a loss of functionality.
* If you want to try playing around as another (fake) user you will need to create a superuser with python manage.py createsuperuser.  
* Once you have a superuser go to localhost:8000/admin and login.  If you select raters you will see a full list of raters.  Their usernames will be in the far right column.  
* Pick any username you like, their passwords are all 'password' for ease of access.
