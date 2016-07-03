from django.contrib import admin

from .models import Consumer
from .models import Merchant
from .models import Product
from .models import ListProduct
from .models import MerchantTender
from .models import ConsumerNotification
from .models import MerchantNotification
from .models import Zone


admin.site.register(Consumer)
admin.site.register(Merchant)
admin.site.register(Product)
admin.site.register(ListProduct)
admin.site.register(MerchantTender)
admin.site.register(ConsumerNotification)
admin.site.register(MerchantNotification)
admin.site.register(Zone)