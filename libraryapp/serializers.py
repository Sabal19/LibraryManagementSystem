from rest_framework import serializers
from datetime import datetime
from .models import Book,BorrowedBooks, BookDetails


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields= '__all__'


class BorrowedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedBooks
        fields= '__all__'

class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookDetails
        fields= '__all__'