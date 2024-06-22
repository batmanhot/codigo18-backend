from django.contrib import admin
from .models import Product, Category

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','description','price','stock','category')
    list_filter = ('category',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
