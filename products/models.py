import datetime
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
    quantity=models.IntegerField()
    pub_date = models.DateTimeField('date published')
    
    
    def __str__(self):
        return self.name
        return self.desc
        return self.price
        return self.offer
        return self.shirt_sizes
        return self.size
        return self.quantity
    
    


    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    

    
