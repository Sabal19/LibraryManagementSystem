
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView

from .models import Book, BookDetails
from .serializers import BookSerializer,BookDetailSerializer

class ModelListCreateView(ListAPIView,CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class ModelUpdateDeleteView(UpdateAPIView,DestroyAPIView,RetrieveAPIView):
    queryset = Book.objects.all()
    
    serializer_class = BookSerializer
    

    def perform_update(self, serializer):
        instance = self.get_object()
        serializer.save()
        

class DetailModelUpdateDeleteView(UpdateAPIView,DestroyAPIView,RetrieveAPIView):
    queryset = Book.objects.all()
    
    serializer_class = BookDetailSerializer
    
    def get_queryset(self):
        books = Book.objects.get(pk=self.kwargs.get('pk', None))
        details = BookDetails.objects.filter(BookID= books)
        return details
    
    # def perform_update(self, serializer):
    #     instance = self.get_object()
    #     serializer.save()