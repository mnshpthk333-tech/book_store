from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.db.models import Avg, Min, Max

# Create your views here.

def index(request):
    books=Book.objects.all().order_by("-rating")
    num_book=books.count()
    avg=books.aggregate(Avg("rating"), Min("rating"), Max("rating"))
    return render(request, "book_outlet/index.html",{
        "books":books,
        "num_books":num_book,
        "avg":avg
    })

def book_details(request, slug):
    books=Book.objects.get(slug=slug)
    return render(request, 'book_outlet/book_detail.html',{
        "title":books.title,
        "rating":books.rating,
        "is_bestseller":books.is_bestselling
    })