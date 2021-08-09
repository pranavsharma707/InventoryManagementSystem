from django.contrib import admin
from .models import Product
from django.contrib.auth.models import Group
# Register your models here
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','category','quantity')
    list_filter=('category',)  # provide a filter header with category field when we click on Product table in admin


admin.site.site_header='KenInventory Dashboard'
admin.site.register(Product,ProductAdmin)
# admin.site.unregister(Group)