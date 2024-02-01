from django.db import models
from django.conf import settings
from account.models import User
from datetime import datetime


# Create your models here.

class Book(models.Model):
    BookID = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=50, blank=False)
    ISBN = models.CharField(max_length=20, unique=True)
    PublishedDate = models.DateField(null=True)
    Genre = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.Title
    

class BookDetails(models.Model):
    
    DetailsID = models.IntegerField(primary_key=True)
    BookID = models.OneToOneField(Book, on_delete=models.CASCADE)  #Here bookdetails and book models show one to one relationship ie. one element of book can only be linked to one element of book detail.
    NumberOfPages = models.IntegerField(null=True)
    Publisher = models.CharField(max_length=255,blank=True)
    Language = models.CharField(max_length=50, blank=True)

class BorrowedBooks(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True) 
    BookID = models.ForeignKey(Book, on_delete=models.CASCADE,null=True,blank=True)
    BorrowDate = models.DateField(null=True, blank=True)
    ReturnDate = models.DateField(null=True, blank=True)
  