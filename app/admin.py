from django.contrib import admin

# Register your models here.
from app.models import *

admin.site.register(UserProfile)




#Now goto setting.py to register u r ----AUTH_USER_MODEL=UserProfile