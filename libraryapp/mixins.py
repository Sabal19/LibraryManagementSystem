from rest_framework.generics import GenericAPIView

from rest_framework import mixins
from .models import BorrowedBooks, Book
from .serializers import BorrowedBookSerializer




class CreateListMixinView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):

    serializer_class = BorrowedBookSerializer
    queryset = BorrowedBooks.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class UpdateDeleteMixinView(mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin,GenericAPIView):
    serializer_class = BorrowedBookSerializer
    queryset = BorrowedBooks.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

