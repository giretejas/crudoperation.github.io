from django.contrib import admin
from .models import Data

# Register your models here.
@admin.register(Data)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','rollno','name','middle','surname','mobileno','email','address','password')
    
