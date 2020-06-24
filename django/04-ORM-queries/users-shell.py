from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    #magic method, will be auto called, when the user obj is called
    def __str__(self):
        s = '\n'
        s += f"first_name: {self.first_name}\n"
        s += f"last_name: {self.last_name}\n"
        s += f"email_address: {self.email_address}\n"
        s += f"age: {self.age}"
        return s
"""
#   Create a model called User following the ERD above
#   Create and run the migration files to create the User table in your database
    python3 manage.py migrate
    python3 manage.py makemigrations
    python3 manage.py shell
    from users_app.models import *

#   Query: Create 3 new users
    User.objects.create(first_name="George", last_name="Serious",email_address="Jora@gmail.com", age="54")
    User.objects.create(first_name="Sam", last_name="Sallick",email_address="Slick_sam@gmail.com", age="15")
    User.objects.create(first_name="Sarah", last_name="Parker",email_address="sarah_sam@gmail.com", age="33")

#    user_temp = User.objects.create(first_name="TEMP", last_name="TEMP",email_address="TEMP@gmail.com", age="100")
#    user_temp.first_name = "wont see me" 
#    exit()
#    python3 manage.py shell
#    user_temp.firstName #ERROR, vars are temp !

#   Query: Retrieve all the users
    User.objects.alll()
    #returns the list of user obj [<User: User object (1)>, <User: User object (2)>, <User: User object (3)>]

#   Query: Retrieve the first user
    User.objects.all().first()
#   Query: Retrieve the last user
    User.objects.all().last()
    User.objects.get(id=1).__dict__

#   Query: Change the user with id=3 so their last name is Pancakes.
    new_user = User.objects.get(id = 3)
    new_user.last_name = "Pancakes"
    new_user.save()

#   Query: Delete the user with id=2 from the database
    temp_user = User.objects.get(id = 2)
    temp_user.detele();

#   Query: Get all the users, sorted by their first name
    User.objects.all().order_by("last_name")

#   BONUS Query: Get all the users, sorted by their first name in descending order
    User.objects.all().order_by('-first_name')

