from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View """

    # serializer_class = serializers.HelloSerializers

    def get(self,request,format=None):

        an_apiview = [
            'Uses HTTP method as functions - get, post, patch, put, delete',
            'It is similar to traditional django view',
            'Gives you the most control over you logic',
            'It mapped manually to the URLs'
        ]

        return Response({'message':'Hello',  'an_apiview': an_apiview})
