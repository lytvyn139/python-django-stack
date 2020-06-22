from django.db import models
import re, bcrypt

class userManager(models.Manager):
    def register_validator(self,postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be filled out and at least 2 characters long!"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be filled out and at least 2 characters long!"
        if not EMAIL_REGEX.match(postData['email']):         
            errors['email'] = "Invalid email address!"
        elif len(User.objects.filter(email=postData['email'])) > 0:
            errors['existingEmail'] = "Email is already taken by another user"
        if len(postData['pw']) < 8:
            errors['pw'] = "Password must be at least 8 characters!"
        elif postData['pw'] != postData['confirm_pw']:
            errors['confirm_pw'] = "Password does not match confirm password field!"
        return errors

    def login_validator(self,postData):
        errors = {}
        user = User.objects.filter(email=postData['email'])
        if len(user) < 1:
            errors['emailDoesNotExist'] = "Email does not exist"
        else:
            logged_user = user[0]
            if not bcrypt.checkpw(postData['pw'].encode(), logged_user.password.encode()):
                errors['badPW'] = "Password is incorrect!!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = userManager()

""" 
login/pass
ksmith@gmail.com
"""