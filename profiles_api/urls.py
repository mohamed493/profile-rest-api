from django.urls import path ,include
from rest_framework import urlpatterns
from . import views

from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register("profile",views.UserProfileViewSet)

urlpatterns=[
    path("login/",views.UserLoginApiView.as_view()) ,
    path("",include(router.urls))
]