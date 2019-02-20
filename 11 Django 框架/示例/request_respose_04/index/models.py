from django.db import models

# Create your models here.

class Users(models.Model):
    uname = models.CharField(max_length=30)
    upwd = models.CharField(max_length=24)
    uemail = models.EmailField(null=True)
    uage = models.IntegerField()

    def __str__(self):
        return self.uname

    class Meta:
        db_table = "Users"
