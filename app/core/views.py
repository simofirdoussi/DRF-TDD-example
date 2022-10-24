"""
Core app views.
"""
from rest_framework import mixins, viewsets

from core.models import Book
from core.serializers import BookSerializer


class BookViewset(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    """Books viewset."""

    serializer_class = BookSerializer
    queryset = Book.objects.all()
