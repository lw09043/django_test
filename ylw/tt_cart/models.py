#coding=utf-8
from django.db import models

class CartInfo(models.Model):
    user=models.ForeignKey('tt_user.UserInfo')
    goods=models.ForeignKey('tt_goods.GoodsInfo')
    count=models.IntegerField()
#谁买了几个什么
