from django.contrib import admin

# Register your models here.
from .models import Categories, Products, Feedback, Order


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category')
    search_fields = ['title']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Order)
admin.site.register(Feedback)

admin.site.site_header = "E-Pak Wholesaler Admin site"
