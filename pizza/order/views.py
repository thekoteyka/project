from django.shortcuts import render, redirect
from pizza.models import PizzaModel
from .forms import CreateForm, CreateOrderModelForm
from .models import OrderModel

# Create your views here.

def create_order(request, *args, **kwargs):
    pizzas = PizzaModel.objects.all()
    order_form = CreateForm(request.POST or None)

    print(order_form.data)
    if order_form.is_valid():
        address = order_form.cleaned_data.get('address')
        order = dict(order_form.data).get('choice')
        pizza_objects = [PizzaModel.objects.get(id=i) for i in order]
        print(pizza_objects)
        
        new_order = OrderModel.objects.create(address=address)
        new_order.pizza_order.add(*pizza_objects)

        new_order.save()
        return redirect('createorder')

    context = {
        'pizzas': pizzas,
        'order_form': order_form
    }
    return render(request, 'order/create_order.html', context)

def create_model_order(request, *args, **kwargs):
    pizzas = PizzaModel.objects.all()
    model_form = CreateOrderModelForm(request.POST or None)
    context = {
        'pizzas': pizzas,
        'modelform': model_form
    }
    return render(request, 'order/create_model_order.html', context)