from rest_framework import serializers
from .models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    """Serializer to show book details along with author name while allowing creation with ID."""
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), write_only=True)  # Accepts ID in API
    author_name = serializers.StringRelatedField(source="author", read_only=True)  # Shows author name

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'author_name', 'published_date']


class AuthorSerializer(serializers.ModelSerializer):
    """Serializer to show author details and related books."""
    books = serializers.SerializerMethodField()  # Custom field for related books

    class Meta:
        model = Author
        fields = ['id', 'name','bio', 'books']  # Include related books in the response

    def get_books(self, obj):
        """Get related books for this author"""
        books = obj.books.all()  # `book_set` is auto-created by Django for reverse FK
        return BookSerializer(books, many=True).data  # Serialize related books
