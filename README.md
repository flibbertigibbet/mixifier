mixifier
========

Django website for mixing together two songs using the [Echonest Remix API](http://echonest.github.io/remix/ "Echonest Remix").  
Uses the [afromb.py example file](https://github.com/echonest/remix/blob/master/examples/afromb/afromb.py "afromb").

Built during [Music Hackday Philly 2013](https://www.hackerleague.org/hackathons/music-hack-day-philly-2013/hacks/mixifier "Hackerleague project page").

Intended for local use; not configured for deployment on a server.

To use:  
1. Install the dependencies in a virtual environment:  django, pyechonest, numpy, remix, and celery.  
2. Add a file named 'secrets.py' to the 'mixifier' directory.  In the file, define ECHO_NEST_API_KEY  
([your API key](http://developer.echonest.com/ "get an API key")), and DJANGO_SECRET_KEY (a random, unique string for your web app).  
3. Put the .mp3 files you want available for remixing into the mixifier/media directory.  
4. Before running app for the first time, initialize the database with:  
```bash
./manage.py syncdb
```
To run, first start celery in one terminal with:
```bash
./manage.py celery worker --loglevel=info
```
Then in a second terminal, start the django server with:
```bash
./manage.py runserver
```
