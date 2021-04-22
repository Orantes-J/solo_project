from django.db import models
import re
# Create your models here.
class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 3:
            errors['first_name'] = "First Name Must Be At Least 3 Characters Long"
        if len(postData['last_name']) < 3 :
            errors['last_name'] = "Last Name Must Be At Least 3 Characters Long"
        if len(postData['username']) < 2 :
            errors['username'] = "Username Must Be At Least 2 Characters Long"
        EMAIL_REGEX =  re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "This Email Does Not Pass The Validation Test"
        if len(postData['password']) < 8 :
            errors['password'] = "Password Must Be At Least 8 Characters Long"
        if not postData['password'] == postData['confirm_password']:
            errors['confirm_pw'] = 'Password Does Not Match'
        return errors


class User(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 70)
    username = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    profile_pic = models.ImageField(upload_to= "static/images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Profile(models.Model):
    my_profile = models.ForeignKey(User, related_name = "profile_obj", on_delete = models.CASCADE)
    profile_banner = models.ImageField(upload_to= "static/images/")
    instagram  = models.CharField(max_length = 70, default = None)
    facebook  = models.CharField(max_length = 70, default = None)
    youtube  = models.CharField(max_length = 70,default = None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class CharacterManager(models.Manager):
    def character_validator(self, postData):
        errors = {}
        if len(postData['powers'])<6:
            errors['powers'] = "Please Explain In 10 Characters Minimum"
        if len(postData['bio'])<15:
            errors['bio'] = "Please Give Us A Description with at Least 40 words"
        return errors

class Character(models.Model):
    name = models.CharField(max_length = 100)
    date_of_birth = models.DateField()
    powers = models.CharField(max_length = 50)
    bio = models.TextField()
    pic = models.ImageField(upload_to= "static/images/")
    creator = models.ForeignKey(User, related_name = "created_characters", on_delete = models.CASCADE)
    saved_by = models.ManyToManyField(User, related_name = "save_post")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CharacterManager()
