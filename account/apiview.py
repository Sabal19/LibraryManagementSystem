
from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib import messages
from rest_framework import status
# from rest_framework import viewsets
from .models import User
from .serializers import PersonalDetailSerializer







@api_view(['GET','POST'])
def Detail(request,pk=None):
    if request.method == 'GET':
        
        detail = User.objects.all()
        serializer = PersonalDetailSerializer(detail,many=True)
        # print(serializer)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
    
    elif(request.method == 'POST'):
        serializers = PersonalDetailSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET'])
def DetailbyID(request, pk):
    try:
        user = User.objects.get(id=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = PersonalDetailSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)