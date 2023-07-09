from django.contrib.auth.models import AbstractUser
from django.db import models

class WebsiteUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    number = models.CharField(max_length=20, null=True, blank=True)
    cat_colour = models.CharField(max_length=50, null=True, blank=True)
    favourite_movie = models.CharField(max_length=100, null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)




