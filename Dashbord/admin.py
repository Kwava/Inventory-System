from django.contrib import admin
from Dashbord.models import Order,Product
from django.contrib.auth.models import Group


# Register your models here.
admin.site.site_header='Inventory Sysrem'
admin.site.unregister(Group)



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','category')
admin.site.register(Product,ProductAdmin)
   

class OrderAdmin(admin.ModelAdmin):
    list_display=('product','staff')
admin.site.register(Order,OrderAdmin)

    

    




