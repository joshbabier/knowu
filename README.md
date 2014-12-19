# KnowU Task:
This is a very simple Django project for grabbing geolocation data for US state counties from the http://api.sba.gov site.

It currently features:

* User login & authentication
* The ability select geolocation data for the counties in any state or all states
* A stand-alone module that writes county geolocation data for all states into a text file in pretty printed JSON.
* Django's default admin.

You can view the project [here](http://54.165.212.2/)

Tests are in the state_scraper/tests directory and can be run from outer project directory with the following commands:
    
    workon knowu
    python manage.py test