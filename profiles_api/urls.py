from django.urls import path ,include
from rest_framework import urlpatterns
from . import views

from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register("profile",views.UserProfileViewSet)

urlpatterns=[
    path("",include(router.urls))
]