from django.db import models


class Contact(models.Model):
        name = models.CharField(max_length=150)
        subject = models.CharField(max_length=250)
        email = models.EmailField(max_length=100)
        message = models.TextField(null=True, blank=True)
