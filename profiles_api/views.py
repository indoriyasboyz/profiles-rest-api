from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status

from profiles_api import serializers
# Create your views here.

class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """retun the list of Api View feactures"""
        an_apiview = [
            'Uses HTTP method as function(get, post, patch, delete, put)',
            'Is similar to traditional Django View',
            'Gives you the most control over your application logic',
            'Is Mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})


    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """"handling updating of  object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """handle partial update of object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """delete an object"""
        return Response({'method': 'DELETE'})
