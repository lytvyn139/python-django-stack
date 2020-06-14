
from django.db import models

class Wizard(models.Model):
    name = models.CharField(max_length=45)
    house = models.CharField(max_length=45)
    pet = models.CharField(max_length=45)
    year = models.IntegerField()

""" 
python manage.py makemigrations
python manage.py migrate
python manage.py shell
from djangoORMapp.models import *

######################################
#   INSERT INTO Wizard (name, house, pet, year) VALUES ('Harry Potter', 'Gryffindor', 'Hedwig', '5');
Wizard.objects.create(name="Harry Potter", house="Gryffindor", pet="Hedwig", year="5")

######################################
#   INSERT INTO Wizard (name, house, pet, year) VALUES ('Hermione Granger', 'Gryffindor', 'Crookshanks', '5');
Wizard.objects.create(name="Hermione Granger", house="Gryffindor", pet="Crookshanks", year="5")

######################################
#    SELECT * FROM Wizard WHERE id = 1;
Wizard.objects.get(id = 1).name

######################################
#   SELECT * FROM Wizard WHERE house = 'Gryffindor';
house = Wizard.objects.filter(house="Gryffindor")
house
######################################
#   UPDATE Wizard SET year = '6' WHERE id = 1;
luna = Wizard.objects.get(name="Hermione Granger")
luna.year = 6
luna.save()



"""

    