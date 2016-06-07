# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_product_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='managers',
            field=models.ManyToManyField(related_name='managers_products', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
