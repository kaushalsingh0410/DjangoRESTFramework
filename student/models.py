from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    std = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name