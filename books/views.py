import requests
from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework import status, filters
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from books.forms import ImportBooksForm
from books.models import Book, Author, Category
from books.serializers import BookSerializer


# Create your views here.


class ImportBookView(APIView):
    """
    Import new books from google API
    and save it in to the database.
    """

    def get(self, request):
        form = ImportBooksForm()
        return render(request, 'import_books.html', {'form': form})

    def post(self, request):
        form = ImportBooksForm(request.POST)
        if form.is_valid():
            query = request.POST['query']
            book_data = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={query}')
            result = book_data.json()
            for item in result['items']:
                if Book.objects.filter(title=item['volumeInfo']['title']):
                    messages.warning(request, f"Books with '{query}' key have been already imported")
                    return render(request, 'import_books.html', {'form': form})
                else:
                    new_book = Book(title=item['volumeInfo'].get('title'),
                                    published_date=item['volumeInfo'].get('publishedDate'),
                                    average_rating=item['volumeInfo'].get('averageRating'),
                                    ratings_count=item['volumeInfo'].get('ratingsCount'),
                                    thumbnail=item['volumeInfo']['imageLinks']['thumbnail']
                                    )
                    new_book.save()
                if 'authors' in item['volumeInfo']:
                    for author in item['volumeInfo'].get('authors'):
                        author_name = Author.objects.get_or_create(author=author)[0]
                        new_book.authors.add(author_name)
                    if 'categories' in item['volumeInfo']:
                        for category in item['volumeInfo'].get('categories'):
                            category_tag = Category.objects.get_or_create(category=category)[0]
                            new_book.categories.add(category_tag)
                        new_book.save()
                    new_book.save()
                    messages.success(request, 'New books have been imported from API')
                    return redirect('books_list')
        return Response(status=status.HTTP_400_BAD_REQUEST)


class BooksListView(ListAPIView):
    """
    API that allows read-only endpoints to represent a collection of books.
    It allows to filter results by published date or author.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['published_date', 'authors__author']
    ordering_fields = ['published_date']


class BookView(RetrieveUpdateDestroyAPIView):
    """
    API that allows single book to be viewed, update or destroy.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
