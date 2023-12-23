from django.http import HttpResponse
from django.shortcuts import render

data = {
    "movies": [
        {"id": 5, "title": "Jaws", "year": 1969},
        {"id": 6, "title": "Sharknado", "year": 2000},
        {"id": 7, "title": "The Meg", "year": 2000},
    ]
}


# 3 parameters for render - request, template name / location, data dictionary
def movies(request):
    #   return render(request, "movies/movies.html", {"movies": ["movie1", "movie2"]})
    return render(request, "movies/movies.html", data)


def home(request):
    return HttpResponse("Home Page")
