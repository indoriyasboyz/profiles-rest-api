from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """retun the list of Api View feactures"""
        an_apiview = [
            'Uses HTTP method as function(get, post, patch, delete, put)',
            'Is similar to traditional Django View',
            'Gives you the most control over your application logic',
            'Is Mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
