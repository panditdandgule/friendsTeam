from django.db import models

# Create your models here.

class order(models.Model):
    item = models.CharField(max_length=20)
    item_qty = models.IntegerField()
    price = models.DecimalField(max_digits=6,decimal_places=2)

    class Meta:
        db_table = "order_info"

class customer(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    order = models.ForeignKey(order,on_delete=models.CASCADE)

    class Meta:
        db_table = "customer_info"


