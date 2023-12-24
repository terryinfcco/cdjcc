# Import our Model and the Django Admin Stuff

from .models import Movie
from django.contrib import admin

# Now register the model with the admin site
admin.site.register(Movie)
