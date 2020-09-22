from django.db import models

# Create your models here.


class Client(models.Model):

    document = models.PositiveIntegerField()
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=245)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Bill(models.Model):

    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=150)
    nit = models.PositiveIntegerField()
    code = models.PositiveIntegerField()

    def __str__(self):
        return "%s" % (self.company_name)


class Product(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    attribute = models.PositiveIntegerField()

    def __str__(self):
        return "%s" % (self.name)


class BillProduct(models.Model):

    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
