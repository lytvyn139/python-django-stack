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


    #* if you edit models.py, exit the shell and remigrate
    python3 manage.py shell
    from users_app.models import User
        
        # create
    User.objects.create(first_name="George", last_name="Serious",email_address="Jora@gmail.com", age="54")
    User.objects.create(first_name="Sam", last_name="Sallick",email_address="Slick_sam@gmail.com", age="15")
    User.objects.create(first_name="Sarah", last_name="Parker",email_address="sarah_sam@gmail.com", age="33")

    user_temp = User.objects.create(first_name="TEMP", last_name="TEMP",email_address="TEMP@gmail.com", age="100")
    user_temp.first_name = "wont see me" 
    exit()
    python3 manage.py shell
    user_temp.firstName #ERROR, vars are temp !

        # display
    User.objects.alll()
    #returns the list of user obj [<User: User object (1)>, <User: User object (2)>, <User: User object (3)>]

    User.objects.all().first()
    User.objects.all().last()
    User.objects.get(id=1).__dict__

        # update
    new_user = User.objects.get(id = 3)
    new_user.last_name = "Pancakes"
    new_user.save()

        #delete
    temp_user = User.objects.get(id = 2)
    temp_user.detele();

        #sorting
    #sort by first name
    User.objects.all().order_by("last_name")
    #sorted by first name in desc order
    User.objects.all().order_by('-first_name')

