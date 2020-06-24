from django.db import models
import re	

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        date_validator = re.compile(r'^(19|20)\d\d([- /.])(0[1-9]|1[012])\2(0[1-9]|[12][0-9]|3[01])$')
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Show name should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Show network should be at least 3 characters"
        if not date_validator.match(postData['release_date']):          
            errors['release_date'] = "Date should be YYYY-MM-DD"
        if len(postData['desc']) < 4:
            errors["desc"] = "Show description should be at least 4 characters"
        return errors

class Show(models.Model): 
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=150)
    release_date = models.DateTimeField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

""" 
python3 manage.py makemigrations
python3 manage.py migrate

python3 manage.py shell
from tvShowsApp.models import *
"""