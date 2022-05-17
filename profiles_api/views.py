from django.shortcuts import render

"""Imports Api View class from the DRF module"""
from rest_framework.views import APIView

"""Imports the response object"""
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test API View"""
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

