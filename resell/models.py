import datetime
from secrets import choice
from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Item(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=150, null=True, blank=True)
    slug = models.SlugField(max_length=50, unique=True)
    brand = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    sku = models.CharField(max_length=150, null=True, blank=True)
    pics = image = models.ImageField(upload_to='items/%Y/%m/%d/id',
                              blank=True)
    code = models.ImageField(blank=True, upload_to='code/%Y/%m/%d')
    location = models.CharField(max_length=150, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

CATEGORY_CHOICES = (
    ('PST', 'Postal'),
    ('SHP', 'Shipping'),
    ('TRV', 'Travel'),
    ('GAS', 'Gas'),
    ('FOD', 'Food'),
    ('OFC', 'Office'),
    ('MSC', 'Misc'),
)
class Expenses(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=150, null=True, blank=True)
    slug = models.SlugField(max_length=50, unique=True)
    item = models.ForeignKey(Item, null=True, blank=True, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    amount = models.DecimalField(max_digits=10,
                                decimal_places=2)
    image = models.ImageField(upload_to='expenses/%Y/%m/%d',
                              blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title