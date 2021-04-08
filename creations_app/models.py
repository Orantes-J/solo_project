from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 70)
    username = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    profile_pic = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Character(models.Model):
    name = models.CharField(max_length = 100)
    date_of_birth = models.DateField()
    powers = models.CharField(max_length = 50)
    bio = models.CharField(max_length = 200)
    pic = models.ImageField(blank=True)
    creator = models.ForeignKey(User, related_name = "created_characters", on_delete = models.CASCADE)
    saved_by = models.ManyToManyField(User, related_name = "save_post")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
