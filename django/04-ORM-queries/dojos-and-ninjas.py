from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Ninja(models.Model):
    dojo_id = models.ForeignKey(Dojo, related_name="student", on_delete = models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

""" 
#SELECT * FROM dojosandninjasApp_ninja;

python3 manage.py makemigrations
python3 manage.py migrate
python manage.py shell
from dojosandninjasApp.models import *

    #Query: Create 3 new dojos
Dojo.objects.create(name="ROCKY", city="Philla", state="PA")
Dojo.objects.create(name="CHICAGO BULLS", city="Chicago", state="IL")
Dojo.objects.create(name="NY YANKEES", city="Brooklyn", state="NY")

    #Query: Delete the 3 dojos you just created
Dojo.objects.all()
Dojo.objects.all().delete()
Dojo.objects.all() # 0

    # Query: Create 3 more dojos
Dojo.objects.create(name="ROCKY", city="Philla", state="PA")
Dojo.objects.create(name="CHICAGO BULLS", city="Chicago", state="IL")
Dojo.objects.create(name="NY YANKEES", city="Brooklyn", state="NY")

    # Query: Create 3 ninjas that belong to the first dojo
    it's 5 now, because ID is autoupdated, and those first 3 dojos were deleted
Ninja.objects.create(dojo_id=Dojo.objects.get(id=4), first_name="Sam", last_name="Smith")
Ninja.objects.create(dojo_id=Dojo.objects.get(id=4), first_name="Nick", last_name="Voyagers")
Ninja.objects.create(dojo_id=Dojo.objects.get(id=4), first_name="Samuel", last_name="Koletzki")

    # Query: Create 3 ninjas that belong to the second dojo
Ninja.objects.create(dojo_id=Dojo.objects.get(id=5), first_name="Lack", last_name="You")
Ninja.objects.create(dojo_id=Dojo.objects.get(id=5), first_name="of", last_name="like")
Ninja.objects.create(dojo_id=Dojo.objects.get(id=5), first_name="fantasy", last_name="That")

    
    # Query: Create 3 ninjas that belong to the third dojo
Ninja.objects.create(dojo_id=Dojo.objects.get(id=6), first_name="Same", last_name="last")
Ninja.objects.create(dojo_id=Dojo.objects.get(id=6), first_name="Name", last_name="of")
Ninja.objects.create(dojo_id=Dojo.objects.get(id=6), first_name="Every where", last_name="immortals")

    # Query: Retrieve all the ninjas from the first dojo
Dojo.objects.first().student.all()
#<QuerySet [<Ninja: Ninja object (1)>, <Ninja: Ninja object (2)>, <Ninja: Ninja object (3)>]>

    # Query: Retrieve all the ninjas from the last
Dojo.objects.last().student.all()
#[<Ninja: Ninja object (7)>, <Ninja: Ninja object (8)>, <Ninja: Ninja object (9)>]>

    # Query: Retrieve the last ninja's dojo
Ninja.objects.get(id=1).last_name

    #  Add a new text field called "desc" to your Dojo class
python3 manage.py migrate
    
    
Dojo.objects.get(id=4).first_name
Dojo.objects.get(id=1).last_name

models.py add make sure null is true
desc = models.TextField(null=True)
select 2, then migrate db

Dojo.objects.create(name="NEW", city="Magic City", state="HA", desc="what ever it's friday my dudes")
"""
