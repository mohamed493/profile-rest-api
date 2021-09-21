from django.conf import settings
from profiles_api import serializers
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status ,viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from rest_framework import filters

from . import models ,permissions


# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.UserProfileSerializers
    queryset=models.UserProfile.objects.all()
    print(queryset)
    print("888888888888bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbhgnb 888")
    authentication_classes=(TokenAuthentication ,)
    permissions_classes=(permissions.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=("name" ,"email" ,)


class UserLoginApiView(ObtainAuthToken):
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES
