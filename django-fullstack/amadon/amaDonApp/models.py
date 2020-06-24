from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Product: {} {}>".format(self.name, self.price)

class Order(models.Model):
    quantity_ordered = models.IntegerField()
    total_price = models.DecimalField(decimal_places=2, max_digits=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<Order: {} {}>".format(self.quantity_ordered, self.total_price)

""" 
rm db.sqlite3
python3 manage.py makemigrations
python3 manage.py migrate

python3 manage.py shell
from amaDonApp.models import *
# create
Product.objects.create(name="notebook",price="5") 
Product.objects.create(name="pen",price="4") 
Product.objects.create(name="eraser",price="1") 

Product.objects.all()
Product.objects.all().delete()
Order.objects.all().delete()
"""