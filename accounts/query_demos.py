from django.db import models
from .models import Customer, Order, Product

customers = Customer.objects.all()

first_customer = Customer.objects.first()

last_customer = Customer.objects.last()

customer_by_name = Customer.objects.get(name="test")

customer_by_id = Customer.objects.get(id=4)

first_customer.order_set.all()

order = Order.objects.first()
parent_name = order.customer.name

products = Product.objects.filter(category='Indoor') 

least_to_greatest = Product.objects.all().order_by('id') 
greatest_to_least = Product.objects.all().order_by('-id')

product_filtered = Product.objects.filter(tags__name="Sports")

all_orders = first_customer.order_set.filter(product__name="Ball").count()

all_orders = {}

for order in first_customer.order_set.all():
    if order.product.name in all_orders:
        all_orders[order.product.name] += 1
    else:
        all_orders[order.product.name] = 1


class ParentModel(models.Model):
    name = models.CharField(max_length=200, null=True)

class ChildModel(models.Model):
    parent = models.ForeignKey(ParentModel)
    name = models.CharField(max_length=200, null=True)

parent = ParentModel.objects.first()
parent.childmodel__set.all()

