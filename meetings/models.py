from django.db import models
from datetime import time

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=50)
    floor_number = models.IntegerField(default=1)
    room_number = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name}: room {self.room_number} on floor {self.floor_number}"
        
class Meeting(models.Model):
    title = models.CharField(max_length=200) # making a database column for a title column to store text
    date = models.DateField() # making a database column for a date column where you can store the date
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"

