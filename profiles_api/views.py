from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status


class HelloApiView(APIView):
    """Test API View """

    serializer_class = serializers.HelloSerializers

    def get(self,request,format=None):

        an_apiview = [
            'Uses HTTP method as functions - get, post, patch, put, delete',
            'It is similar to traditional django view',
            'Gives you the most control over you logic',
            'It mapped manually to the URLs'
        ]

        return Response({'message':'Hello',  'an_apiview': an_apiview})

    def post(self, request, pk=None):

        serializer = self.serializer_class(data=request.data)

        if(serializer.is_valid()):
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message' : message})
        else:
            return Response(
                serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """ Handles updating an object"""

        return Response({'method': 'put'})

    def patch(self, request, pk=None):
        """ Patch request. Only handles fields provided in the request"""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """ Deletes an object"""

        return Response({'method': 'delete'})
