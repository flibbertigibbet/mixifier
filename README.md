mixifier
========

Django website for mixing together two songs using the Echonest Remix API.
Uses the afromb.py example file:
https://github.com/echonest/remix/blob/master/examples/afromb/afromb.py

Intended for local use; not configured for deployment on a server.

To use:
1.  Install the dependencies in a virtual environment:  django, pyechonest,
numpy, remix, and celery.
2.  Add a file named 'secrets.py' the 'mixifier' directory.  In the file, define
ECHO_NEST_API_KEY (your API key) and DJANGO_SECRET_KEY (a random, unique string
for your web app).
3.  To run, first start celery in one terminal with:
```bash
./manage.py celery worker --loglevel=info
```
Then in a second terminal, start the django server with:
```bash
./manage.py celery worker --loglevel=info
```

