from django.db import models

class Birthdays(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    birth_date=models.DateField()
    date_added=models.DateTimeField(auto_now_add=True)


