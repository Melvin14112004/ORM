from django.db import models
from django.contrib import admin
class Player (models.Model):
    pid=models.CharField(max_length=20,help_text="Player ID")
    name=models.CharField(max_length=100)
    height=models.IntegerField()
    weight=models.IntegerField()
    phone_no=models.IntegerField()

class PlayerAdmin(admin.ModelAdmin):
    list_display=('pid','name','height','weight','phone_no')
