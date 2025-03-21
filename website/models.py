from django.conf import settings
from django.db import models
from django.utils import timezone
from dateutil.relativedelta import relativedelta


class Student(models.Model):
    Student_ID = models.IntegerField(primary_key = True)
    Name = models.CharField(max_length=200)
    Department = models.TextField()
    phone_number = models.IntegerField()
    DOB = models.DateField()
    age = models.IntegerField()

    def calculate_age(self):
        self.age=relativedelta(timezone.now().date(), self.DOB).years

    def __str__(self):
        return self.Name