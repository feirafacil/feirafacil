from django.contrib import admin

from .models import Consumer
from .models import Merchant

admin.site.register(Consumer)
admin.site.register(Merchant)