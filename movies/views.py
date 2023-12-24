from django.http import HttpResponse
from django.shortcuts import render

# Have to import the Movie class from model.py
from .models import Movie


# 3 parameters for render - request, template name / location, data dictionary
def movies(request):
    # Get all the objects from the database
    data = Movie.objects.all()
    # Have to convert the queryset data to a dictionary which he called movies
    return render(request, "movies/movies.html", {"movies": data})


def home(request):
    return HttpResponse("Home Page")


def detail(request, id):
    # This time the data is one record. The id will come from the url when the user clicks on a movie name
    data = Movie.objects.get(pk=id)
    return render(request, "movies/detail.html", {"movie": data})
