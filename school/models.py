from django.db import models

from base.models import BaseModel

# Create your models here.


class School(BaseModel):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    website = models.URLField()
    logo = models.ImageField(upload_to="media/school_logo")

    def __str__(self):
        return self.name
