from django.http import HttpResponse
from django.shortcuts import render

from .models import Author, Genre, Book, BookInstance


def index(request):
    numBooks = Book.objects.all().count()
    numBookInstances = BookInstance.objects.all().count()
    numAuthors = Author.objects.all().count()

    available = BookInstance.objects.filter(status__exact='a').count()

    return render(
        request,
        'index.html',
        context={
            'numBooks': numBooks,
            'numBookInstances': numBookInstances,
            'numAuthors': numAuthors,
            'available': available
        }
    )
