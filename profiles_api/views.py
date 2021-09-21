from django.conf import settings
from profiles_api import serializers
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status ,viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from rest_framework import filters

from . import models ,permissions


# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.UserProfileSerializers
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=("name" ,"email" ,)
    print(queryset)
    print("888888888888bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbhgnb 888")


class UserLoginApiView(ObtainAuthToken):
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    authentication_classes=(TokenAuthentication,)
   # permissions_classes=(permissions.UpdateOwnProfile,)
    serializer_class=serializers.ProfileFeedItemSerializers
    queryset=models.ProfileFeedItem.objects.all()
    permission_classes=(
        permissions.UpdateOwnStatus,
        IsAuthenticated,

    )

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)
    





