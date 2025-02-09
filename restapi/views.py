'''
from django.shortcuts import render
from rest_framework import generics
from .models import Content
from .serializers import ContentSerializer

# Create your views here.

class ContentListCreate(generics.ListCreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class ContentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_field = "pk"
'''

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Content
from .serializers import ContentSerializer


@api_view(['GET'])
def get_contents(request):
    content = Content.objects.all()
    serializer = ContentSerializer(content,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_content(request):
    serializer = ContentSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def content_detail(request,pk):
    try:
        content = Content.objects.get(pk=pk)
        serializer = ContentSerializer(content)
    except Content.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ContentSerializer(content)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ContentSerializer(content,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        content.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

