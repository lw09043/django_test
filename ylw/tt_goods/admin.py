from django.contrib import admin
from .models import GoodsInfo,TypeInfo
from ylw.urls import admin

admin.site.register(GoodsInfo)
admin.site.register(TypeInfo)

