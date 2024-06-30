from django.db import models


# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=250)
    email_address = models.EmailField()
    message = models.TextField(max_length=3000)

    def __str__(self):
        return self.email_address
