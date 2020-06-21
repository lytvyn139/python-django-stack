from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def regValidator(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        emailTaken = User.objects.filter(email = postData['form_email'])
        print("print postData paramater below!!")
        print(postData)
        errors = {}
        #code to validate the info from form (postData)
        #name is required
        if len(postData['form_name']) == 0:
            errors['nameReq'] = "Name is required!"
        #email is required
        if len(postData['form_email']) == 0:
            errors['emailReq'] = "Email is required!"
        # if they put in email, check to see if email exists in the database already, if it does, then the email is already taken and they must pick another email address
        # ClassName.objects.filter(field1="value for field1", etc.) - gets any records matching the query provided
        # print("PRINTING THE EMAIL FILTER BELOW!!")
        # print(User.objects.filter(email = postData['form_email']))

        elif len(emailTaken)>0: 
            errors['tryanotheremail'] = "This email is already taken, please try another email"
        #pw must be at least 4 characters long
        elif not EMAIL_REGEX.match(postData['form_email']):
            errors['invalidEmail'] = "This is not a real email. Who you tryna fool!"
        if len(postData['pw']) < 4:
            errors['pw'] = "Password needs to be at least 4 characters!"
        #confirm pw must be same as password
        if postData['pw'] != postData['cpw']:
            errors['cpw'] = "Password and confirm password must match"

        return errors
    
    def loginvalidator(self, postData):
        print("in the login validator!!")
        print(postData)
        emailMatch = User.objects.filter(email = postData['form_email'] )
        print(emailMatch) 
        # <QuerySet []> if no users in db match the email from login form this is what the emailmatch variable looks like
        errors = {}
        # validation code for login
        if len(postData['form_email']) == 0:
            errors['emailReq'] = "Email is required"
        #check to see if the email they typed exists in db
        if len(emailMatch) == 0:
            errors['emailNotFound'] = "Email is not registered, please register first"
        #if the email does exist in the db, then get that users password and compare it with the attempted password from the form
        else:
            print("we found a user that matches that email")
            print(emailMatch[0].password)
            if bcrypt.checkpw(postData['pw'].encode(), emailMatch[0].password.encode()):
                print("yayy password match")
            else:
                errors['passwordfailed'] = "Incorrect Password. Please try again."

            # if bcrypt.checkpw(request.POST['password'].encode(), user.pw_hash.encode()):
            #     print("password match")
            # else:
            #     print("failed password")



        print(errors)
        return errors
    


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    objects = UserManager()

class Item(models.Model):
    name = models.CharField(max_length = 255)
    uploader = models.ForeignKey(User, related_name = 'items_uploaded', on_delete = models.CASCADE)
    favoritors = models.ManyToManyField(User, related_name = "items_favorited")
    created_at = models.DateTimeField(auto_now_add = True)



