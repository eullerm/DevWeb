from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    fields = ['category', 'name', 'description', 'slug', 'image', 'price', 'registeredDate', 'available', 'bestSeller']
    list_display = ['category', 'name', 'description', 'slug', 'image', 'price', 'registeredDate', 'available', 'bestSeller']
    list_display_links = ['category']
    search_fields = ['name', 'image']
    list_filter = ['category', 'registeredDate']
    list_editable = [ 'image', 'price', 'available', 'bestSeller']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)