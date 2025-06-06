from django.db import models

class Employee(models.Model):
    emp_id = models.CharField(max_length=8)
    name = models.CharField(max_length= 20)
    post = models.CharField(max_length= 20)

    def __str__(self):
        return self.name



