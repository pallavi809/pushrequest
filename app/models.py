from django.db import models

# Create your models here.
class Student(models.Model):
    rn=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    marks=models.FloatField()

    def __str__(self):
        return '{self.rn},{self.name},{self.city},{self.marks}'
        

