from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Item(models.Model):
    class Meta(object):
        db_table='item'

    status = models.CharField(
        'Status',blank = False, null = False, max_length = 50, db_index = True
    )
    name = models.CharField(
        'Name',blank = False, null = False,max_length=50,db_index=True
    )
    category = models.CharField(
        'Category', blank = False, null = False,max_length=50,
    )
    price = models.DecimalField(
        'Price',blank = False, null = False, max_digits = 10, decimal_places = 2
    )
    image = CloudinaryField(
        'Image', blank = True, null = True,
    )
    created_at = models.DateTimeField(
        'Created Datetime', blank = True, null = True, auto_now_add = True
    )
    updated_at = models.DateTimeField(
        'Upatded Datetime', blank = True, null = True, auto_now = True
    )

# create class item and create 7 table are  status, name,category,price,image,created_at,updated_at