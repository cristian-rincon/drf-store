from django.db import models
from users.models import User
# Create your models here.


class Bill(models.Model):

    client_id = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=150)
    nit = models.PositiveIntegerField()
    code = models.PositiveIntegerField()

    def __str__(self):
        return "%s" % (self.company_name)


class Product(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    attribute = models.CharField(max_length=200)
    
    def __str__(self):
        return "%s" % (self.name)


class BillProduct(models.Model):

    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
