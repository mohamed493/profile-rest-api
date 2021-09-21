from rest_framework import serializers
from profiles_api import models


class UserProfileSerializers(serializers.ModelSerializer):

    class Meta:
        model=models.UserProfile
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user=models.UserProfile.objects.create_user(
            name=validated_data["name"] ,
            email=validated_data["email"] ,
            password=validated_data["password"] ,

        )
        return user 


class ProfileFeedItemSerializers(serializers.ModelSerializer):

        class Meta:
            model=models.ProfileFeedItem
            fields = '__all__'
            extra_kwargs = {'user_profile': {'read_only': True}}

