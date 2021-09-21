from django.db import models
from django.conf import settings

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser ,PermissionsMixin, UserManager,BaseUserManager

class UserProfileManager(BaseUserManager):

    def create_user(self ,name ,email ,password=None):
        if not email :
            raise ValueError("users must have email address")
        email=self.normalize_email(email)
        user=self.model(email=email ,password=password)
        user.set_password(password)
        user.save(using=self._db)

        return user 

    def create_superuser(self ,name ,email ,password):
        """create super user """
        user=self.create_user(name ,email ,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return user 


    
            



class UserProfile(AbstractBaseUser ,PermissionsMixin):
    """"Database fot the users in the system"""
    email=models.EmailField(max_length=255 ,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserProfileManager()
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["name"]


    def get_full_name(self):
        return self.name
    def get_short_name(self):
        return self.name
    def __str__(self) :
        return self.email 


class ProfileFeedItem(models.Model):
    """""profile status update """
    user_profile=models.ForeignKey(
        settings.AUTH_USER_MODEL ,
        on_delete=models.CASCADE

    )
    status_text=models.CharField(max_length=255)
    create_on=models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return self.status_text
