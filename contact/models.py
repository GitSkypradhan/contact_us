from django.db import models

# Create your models here.
class ContactFrom(models.Model):
    name = models.CharField(max_length=100,default="", )
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=100,default="",)

    def __str__(self):
        return self.name
