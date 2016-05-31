from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(default="Default value")
    price = models.DecimalField(max_digits=100, decimal_places=2, default=9.99)
    sale_price = models.DecimalField(max_digits=100, decimal_places=2, default=6.99, null=True, blank=True)

   # item_id = models.IntegerField()

    def __unicode__(self):
        return self.title


