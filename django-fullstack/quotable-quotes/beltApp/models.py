from django.db import models
import re, bcrypt

class userManager(models.Manager):
    def register_validator(self,postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors = {}
        if len(postData['name']) < 3:
            errors['name'] = "First name must be filled out and at least 3 characters long!"
        if not EMAIL_REGEX.match(postData['email']):         
            errors['email'] = "Invalid email address!"
        elif len(User.objects.filter(email=postData['email'])) > 0:
            errors['existing_email'] = "Email is already taken by another user"
        if len(postData['pw']) < 3:
            errors['pw'] = "Password must be at least 3 characters!"
        elif postData['pw'] != postData['confirm_pw']:
            errors['confirm_pw'] = "Password does not match confirm password field!"
        return errors

    def login_validator(self,postData):
        errors = {}
        user = User.objects.filter(email=postData['email'])
        if len(user) < 1:
            errors['email_doesnt_exits'] = "Email does not exist in our db!"
        else:
            logged_user = user[0]
            if not bcrypt.checkpw(postData['pw'].encode(), logged_user.password.encode()):
                errors['badPW'] = "Password is incorrect!!"
        print(errors)
        return errors

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = userManager()

class quoteManager(models.Manager):
    def quote_validator(self, postData):
        print("\033[1;34;40m ( ̲̅:̲̅:̲̅:̲̅[̲̅ ̲̅]̲̅:̲̅:̲̅:̲̅ ̲̅) DEBUG ( ̲̅:̲̅:̲̅:̲̅[̲̅ ̲̅]̲̅:̲̅:̲̅:̲̅ ̲̅) ")
        print(f'\033[1;31;40m ☠  Quote Manager says: {postData} ☠')
        print("\033[1;34;40m ( ̲̅:̲̅:̲̅:̲̅[̲̅ ̲̅]̲̅:̲̅:̲̅:̲̅ ̲̅) DEBUG ( ̲̅:̲̅:̲̅:̲̅[̲̅ ̲̅]̲̅:̲̅:̲̅:̲̅ ̲̅) ")
        errors = {}
        if len(postData['author']) < 2:
            errors['author_length'] = "Author must be at least 2 characters"
        if len(postData['quote']) < 5:
            errors['quote_length'] = "Quote must be at leat 5 characters"
        print(errors)
        return errors

class Quote(models.Model):
    author = models.CharField(max_length=255)
    quote = models.TextField()
    posted_by = models.ForeignKey(User, related_name="posted_quotes", on_delete=models.CASCADE)
    favorite = models.ManyToManyField(User, related_name="favorite_quote")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = quoteManager()

""" 
EMAIL AS EMAIL AND PASS

oinkoink@gmail.com
Tactical@Tactical.Tactical
10x_DEV@gmail.com
NEWUSER@NEWUSER.COM
"""