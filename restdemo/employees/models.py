from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    company_name = models.CharField(max_length=30)
    age = models.IntegerField()
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=50)
    zip = models.IntegerField()
    email = models.EmailField()
    web = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name +' '+ self.last_name
