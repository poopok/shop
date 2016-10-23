from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Item, Category

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'parent']


class ItemAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'description', 'image_url', 'category']

# Пытался сделать так, что б в админке красиво выводило, но выдавало ошибку:
#
# TemplateDoesNotExist at /admin/search/category/
# admin/mptt_change_list.html
#
# Гуглил проблему, нашёл только советы переустановить или обновить. Не помогло.
#
#
# class CategoryAdmin(MPTTModelAdmin):
#     fields = ['name', 'parent']
#
#
# class ItemAdmin(MPTTModelAdmin):
#     fields = ['name', 'price', 'description', 'image_url', 'category']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
