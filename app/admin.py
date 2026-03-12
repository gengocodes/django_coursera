from django.contrib import admin
from .models import Menuitems, DrinksCategory, Drinks

# Register your models here.
admin.site.register(Menuitems)
admin.site.register(DrinksCategory)
admin.site.register(Drinks)
