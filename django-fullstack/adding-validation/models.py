from django.db import models

class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['name']) < 5:
            errors["name"] = "Blog name should be at least 5 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "Blog description should be at least 10 characters"
        return errors

class Blog(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BlogManager()    # add this line!

# # REGEX VALIDATIOR
# import re
# class BlogManager(models.Manager):
#     def basic_validator(self, postData):
#         EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
#         date_validator = re.compile(r'^(19|20)\d\d([- /.])(0[1-9]|1[012])\2(0[1-9]|[12][0-9]|3[01])$')

#         errors = {}

#         if not EMAIL_REGEX.match(postData['email']): # test whether a field matches the pattern
#         errors['email'] = "Invalid email address!"
#         return errors
#         if not date_validator.match(postData['release_date']):
#         errors['release_date'] = "Date should be in YYYY-MM-DD format"
