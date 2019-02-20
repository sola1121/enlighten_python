from django.contrib import admin

# Register your models here.

from .models import *

class GoodsAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "picture"]
    list_editable = ["title", "picture"]


admin.site.register(Goods, GoodsAdmin)
admin.site.register(GoodType)
admin.site.register(Users)
