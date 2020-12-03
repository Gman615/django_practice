from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    persons = ["Keith David", "Cassius Winston", "Goldie Hawn", "Kurt Russell", "Donald Pleasance"]
    context = {
        'persons': persons
    }
    return render(request, "home.html", context)