"""
Core app serializers
"""
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    """Book model serializer."""

    class Meta:
        fields = ['name', 'description']
