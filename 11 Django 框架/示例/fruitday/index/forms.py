from django import forms

from .models import Users, Goods, GoodType

class UserFrom(forms.ModelForm):
    class Meta:
        model = Users
        fields = ("uphone", "upwd")
        labels = {"uphone": "手机号", "upwd": "密码"}
        widgets = {
            "uphone": forms.TextInput(
                attrs={"placeholder":"请输入手机号", "class": "form-control"}
            ),
            "upwd": forms.PasswordInput(
                attrs={"placeholder": "请输入6-20位号码字符", "class": "form-control"}
            )
        }
