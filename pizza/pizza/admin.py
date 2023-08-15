from django.contrib import admin
from .models import PizzaModel, ToppingModel, PizzaProxy

# Register your models here.


class PizzaInline(admin.StackedInline):
    model = PizzaProxy
    extra = 0
    verbose_name = 'topping'
    verbose_name_plural = 'Create new pizza recipe'

class PizzaAdmin(admin.ModelAdmin):
    inlines = [
        PizzaInline,
    ]
    exclude = 'toppings',
    list_display = 'name', 'all_toppings'

admin.site.register(PizzaModel, PizzaAdmin)
admin.site.register(ToppingModel)

# admin.site.register(PizzaModel) 