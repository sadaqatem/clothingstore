from django.contrib import admin
# from django.contrib.contenttypes.admin import GenericTabularInline

from .models import Product


admin.site.register(Product)