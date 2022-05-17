from django.shortcuts import render

"""Imports Api View class from the DRF module"""
from rest_framework.views import APIView

"""Imports the response object"""
from rest_framework.response import Response

"""Status Codes to be used when returning responses"""
from rest_framework import status

"""Serializer module imported"""
from profiles_api import serializers

""""""
from rest_framework import viewsets
# Create your views here.

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):
        """Return a list of API View Features"""
        """A function for each HTTP request made to the view """
        an_apiview = [
            'Uses HTTP methods as fucntions(get,post, patch, put, delete)'
            'Is similar to a traditional DjangoView',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLS',
        ]
        """In order to convert to JSON, it needs to be a list or dic"""
        return Response({'message': 'Hello', 'An_apiview': an_apiview})

    def post(self, request):
        """Create a Hellow Message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an Object"""
        return Response({"method": 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test AP Viewset"""
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """Return Hello Message """

        a_viewset = [
            'user actions (list, create, retrieve, update, partial update)',
            'auto maps to URLS using routers',
            'more func, with less code',
        ]
        return Response({'message': 'Hello! ', 'a viewset': a_viewset})

    def create(self, request):
        """Create a new Hello Message"""
        serializers = self.serializer_class(data=request.data)

        if serializers.is_valid():
            name = serializers.validated_data.get('name')
            message =f'{name}!'
            return Response({'message': message})
        else:
            return Response(
                serializers.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by is ID """
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'Http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an Object"""
        return Response({'http_method': "PATCH"})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})
