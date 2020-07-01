from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status

from profiles_api import models
from rest_framework import filters
from profiles_api import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from rest_framework.permissions import IsAuthenticatedOrReadOnly


class HelloViewSets(viewsets.ViewSet):
    """Test APi View sets"""

    serializer_class = serializers.HelloSerializers

    def list(self, request):

        an_apiviewsets = [
            'Uses HTTP method as functions - list, create, retrieve, update,partial update, Destroy',
            'It is similar to traditional django viewsets',
            'Gives you the most control over you logic',
            'It mapped manually to the URLs'
        ]

        return Response({'message':'Hello',  'an_apiviewsets': an_apiviewsets})

    def create(self, request):
        serializer =  self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message' : message})
        else:
            return Response(
                    serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handles getting in an object by its Id"""
        return Response({'HTTP method': 'Get'})

    def update(self, request, pk=None):
        """ Handles updating an object"""
        return Response({'HTTP Method': 'PUT'})

    def partial_update(self, request, pk=None):
        """ Handles updating an part of an object"""
        return Response({'HTTP Method': 'PATCH'})

    def destroy(self, request, pk=None):
        """ Handles removing an object """
        return Response({'HTTP Method' : 'DELETE'})


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

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating user profiles"""


    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email', 'address',)

class UserLoginApiView(ObtainAuthToken):
    """ Check Email name and password and returns Auth token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemsSerializer
    queryset = models.ProfileFeedItems.objects.all()
    permission_classes = (
            permissions.UpdateOwnStatus,
            IsAuthenticatedOrReadOnly)

    def perform_create(self, serializers):

        serializers.save(user_profile=self.request.user)
