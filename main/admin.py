from django.contrib import admin

from .models import Consumer

from .models import Product
from .models import ListProduct


admin.site.register(Consumer)

admin.site.register(Product)
admin.site.register(ListProduct)