from django.contrib import admin
from . models import Student

# Register your models here.
class StuAd(admin.ModelAdmin):
    list_display=['rn','name','city','marks']
admin.site.register(Student,StuAd)
