from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=30)
   # item_id = models.IntegerField()

    def __unicode__(self):
        return self.title


