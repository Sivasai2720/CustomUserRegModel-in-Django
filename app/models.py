from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
# Create your models here.
class UserProfileManager(BaseUserManager): #2nd Step to write a code 
    def create_user(self,email,first_name,last_name,password=None):
        if not email:
            raise ValueError('Please Provide Email')

        ne=self.normalize_email(email) #This normalize_email works like Lowercase as output , if u give input capital also bydefaul it convert into lower cases
        UPO=self.model(email=ne,first_name=first_name,last_name=last_name)  #Here we r creating userprofilr object
        UPO.set_password(password)
        UPO.save()
        return UPO #Why we r returning this means we want to use this in Create_superuser, bcz is_staff,superuser bydefult False to make True
    def create_superuser(self,email,first_name,last_name,password):
        UPO=self.create_user(email,first_name,last_name,password)
        UPO.is_staff=True
        UPO.is_superuser=True
        UPO.save()
        #I dont want to Return here bcz i never using any where to make changes in staff and superuser
        #then go to userprofile to register u r created object ---objects=UserProfileManager
        #goto admin.py to register
       






class UserProfile(AbstractBaseUser,PermissionsMixin):   #1st Step to write a code 
    email=models.EmailField(primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    objects=UserProfileManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']

