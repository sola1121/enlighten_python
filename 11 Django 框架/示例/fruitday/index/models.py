from django.db import models

# Create your models here.

# 商品类型
class GoodType(models.Model):
    title = models.CharField(max_length=50)
    picture = models.ImageField(upload_to="static/upload/goodstype")
    dexc = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "GoodType"
        verbose_name = "GoodType"
        verbose_name_plural = verbose_name
     

# 商品
class Goods(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    spec = models.CharField(max_length=25)
    picture = models.ImageField(upload_to="static/upload/goods")
    isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Goods"
        verbose_name = "Goods"
        verbose_name_plural = verbose_name

# 用户
class Users(models.Model):
    uphone = models.CharField(max_length=11)
    upwd = models.CharField(max_length=20)
    uemail = models.EmailField(null=True)
    uname = models.CharField(max_length=30)
    isActive = models.BooleanField(default=True)
    
    def __str__(self):
        return self.uname

    class Meta:
        db_table = "Users"
        verbose_name = "Users"
        verbose_name_plural = verbose_name