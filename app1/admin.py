from django.contrib import admin
from .models import *


class sk(admin.ModelAdmin):
    list_display = ['pk', 'shopkeeper_name', 'password']


admin.site.register(Shopkeeper, sk)
admin.site.register(Shop)
admin.site.register(Purchase)
admin.site.register(Product)
admin.site.register(PurchaseId)
admin.site.register(Consumer)


