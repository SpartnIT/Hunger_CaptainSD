from django.db import models
from apps.items.models import Item

# Create your models here.

class Review(models.Model):
    class Meta(object):
        db_table='review'
    
    item = models.ForeignKey(
        Item , on_delete=models.CASCADE, db_index=True
    )
    name = models.CharField(
        'Name', blank=False, null=False,max_length=20,db_index=True
    )
    body = models.TextField(
        'Body', blank=True,null=True,db_index=True
    )
    like_count = models.IntegerField(
        'Like Count',blank=True,null=True,db_index=True
    )
    created_at = models.DateTimeField(
        'Created at', blank= True, null=True,auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Updated at', blank= True, null= True, auto_now= True
    )
#create class review and add 6 tables that are item,name,body,like_count,creted_at,updated_at