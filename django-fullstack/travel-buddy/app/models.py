from django.db import models
from datetime import date
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        print("\033[1;34;40m ( ̲̅:̲̅:̲̅:̲̅[̲̅ ̲̅]̲̅:̲̅:̲̅:̲̅ ̲̅) creating user: ( ̲̅:̲̅:̲̅:̲̅[̲̅ ̲̅]̲̅:̲̅:̲̅:̲̅ ̲̅) ")
        print(f"\033[1;31;40m ☠  Name: {postData['name']} Login: {postData['username']} ☠")
        if len(postData['name']) < 3:
            errors["name"] = "Name should be at least 3 characters"
        if len(postData['username']) < 3:
            errors["username"] = "Login should be at least 3 characters"
        if len(postData['pwd']) < 5:
            errors["pwd"] = "Password should be at least 5 characters"
        if postData['pwd'] != postData['confirm_pwd']:
            errors['confrim_pwd'] = "Passwords do not match"
        users = User.objects.all()
        for user in users:
            if postData['username'] == user.username:
                errors['username'] = "username is taken"
        return errors

class User(models.Model):
    name = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class PlanManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        print("\033[1;34;40m ( ̲̅:̲̅:̲̅:̲̅[̲̅ ̲̅]̲̅:̲̅:̲̅:̲̅ ̲̅) adding trip ( ̲̅:̲̅:̲̅:̲̅[̲̅ ̲̅]̲̅:̲̅:̲̅:̲̅ ̲̅) ")
        print(f'\033[1;31;40m ☠  Plan Manager: {postData} ☠')
        DATE_REGEX = re.compile(r'(\d{4})-(\d{1,2})-(\d{1,2})')
        if not DATE_REGEX.match(postData['date_from']):            
            errors['date_from'] = "Date must be in format YYYY-MM-DD"
        if not DATE_REGEX.match(postData['date_to']):            
            errors['date_to'] = "To Date must be formatted YYYY-MM-DD"
        if len(postData['destination']) < 1:
            errors["destination"] = "Destination must be filled out !"
        if len(postData['description']) < 1:
            errors["description"] = "Description must be filled out !"
        if postData['date_from'] < str(date.today()):
            errors['date_from_past'] = "Time travel feature is locked"
        if postData['date_from'] > postData['date_to']:
            errors['dates'] = "Date To cannot be before Date From"
        return errors

class TravelPlan(models.Model):
    destination = models.CharField(max_length=45)
    description = models.TextField()
    dateFrom = models.DateField()
    dateTo = models.DateField()
    creator = models.ForeignKey(User, related_name="plans", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PlanManager()

class Trip(models.Model):
    plan = models.ForeignKey(TravelPlan, related_name="trips", on_delete = models.CASCADE)
    users = models.ManyToManyField(User, related_name="users")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

""" 
Rob, one line is login/pass

    YURII90924
    Same_same
    Samwise1
    Sarah1982
    NO_NAMER
    Joseph123
"""
