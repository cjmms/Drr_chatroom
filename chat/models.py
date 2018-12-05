from django.db import models

# Create your models here.

class Room(models.Model):
    room_text = models.CharField(max_length=200)
    def __str__(self):
        return self.room_text

class User(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user_text = models.CharField(max_length=200)
    def __str__(self):
        return self.user_text

        

