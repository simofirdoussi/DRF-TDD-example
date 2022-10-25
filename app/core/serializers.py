"""
Core app serializers
"""
from rest_framework import serializers
from core.models import Book

class BookSerializer(serializers.ModelSerializer):
    """Book model serializer."""

    class Meta:
        model = Book
        fields = '__all__'
