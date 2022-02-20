from re import I
from django.contrib import admin
from b.models import *

# Register your models here.

class Home_Model_Admin(admin.ModelAdmin):
    List_Display = ['id','name','username','password']

admin.site.register(Home_Model,Home_Model_Admin)
