from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)   # food, appliance clothes
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "categories"

class Item(models.Model):
    name = models.CharField(max_length=100)    # food : pizza, hamburger // appliance : air conditioner, dryer
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image_url = models.URLField(null=True, blank=True)
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'items'


class Order(models.Model):
    delivery_address = models.CharField(max_length=100)
    order_date = models.DateTimeField()
    item = models.ManyToManyField('Item', through='ItemOrder')
    def __str__(self):
        return self.delivery_address

    class Meta:
        db_table = 'orders'

class ItemOrder(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    item_count = models.IntegerField()
    def __str__(self):
        return self.order + self.item

    class Meta:
        db_table = 'item_orders'
