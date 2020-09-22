from django.contrib import admin

# Register your models here.
from .models import Bill
from .models import BillProduct
from .models import Product


admin.site.register(Bill)
admin.site.register(BillProduct)
admin.site.register(Product)