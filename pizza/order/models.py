from django.db import models
from pizza.models import PizzaModel

# Create your models here.

class OrderModel(models.Model):
    address = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    pizza_order = models.ManyToManyField(PizzaModel)
    
    def __str__(self):
        order = ', '.join([o.name for o in self.pizza_order.all()])
        return f'Address: {self.address}, Order: {order}'
    
    def all_orders(self):
        return '\n'.join([o.name for o in self.pizza_order.all()])

    class Meta:
        verbose_name = 'Orders'
        verbose_name_plural = 'Orders'

class OrderProxy(OrderModel.pizza_order.through):
    class Meta:
        proxy = True

    def __str__(self):
        return str(self.ordermodel)