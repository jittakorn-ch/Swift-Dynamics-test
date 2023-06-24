from django.db import models

# Create your models here.

class ToDo(models.Model):   # create table name ToDo in Database
    title = models.CharField(max_length=100)    # create field name title 
    description = models.TextField(blank=True)  
    date = models.DateField(blank=False)
    completed = models.BooleanField(default=False)

    def __str__(self):      # ใช้คืนค่าเป็น string ให้ object
        return self.title