"""
Unit tests for core app functionalities.
"""
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.serializers import BookSerializer
from core.models import Book


BOOKS_URL = reverse('book:book-list')


def create_book(**params):
    defaults = {
        'name': 'book name',
        'description': 'book description'
    }
    defaults.update(params)
    return Book.objects.create(
        **defaults
    )


class CoreUnitTests(TestCase):
    """Core app unit tests."""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_books_list(self):
        """Test retrieving a list of books."""

        create_book()
        create_book(name='book 2')
        res = self.client.get(BOOKS_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)

        self.assertEqual(res.data, serializer.data)
