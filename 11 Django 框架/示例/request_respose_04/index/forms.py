from django import forms

from .models import *

# 为topic下拉列表初始化一组数据 - 元组
TOPIC_CHOICE = (
    ("level1", "好评"),
    ("level2", "中评"),
    ("level3", "差评"),
)

class RemarkForm(forms.Form):
    # 1. 创建subject属性, 表示评论标题, 显示成文本框
    # 1.1 label生成控件前面的提示文本
    # 1.2 initial表示初始化的属性, 等同于控件的value属性
    subject = forms.CharField(label="标题", initial="初始数据")
    # 2. 创建email属性, 表示邮箱, 显示成email控件
    email = forms.EmailField(label="邮箱")
    # 3. 创建message属性, 表示评论内容, 显示成多行文本域
    # 3.1 widget让当前控件变为一个多行文本域
    message = forms.CharField(label="内容", widget=forms.Textarea(attrs={"placeholder": "限制在150字内"}))
    # 4. 创建topic属性, 表示评论级别, 显示成一个下拉列表
    # 4.1 choices指定下拉列表选项的数据们
    topic = forms.ChoiceField(label="评价", choices=TOPIC_CHOICE)
    # 5. 创建isSave属性, 表示是否保存, 显示成一个复选框
    isSave = forms.BooleanField(label="是否保存")

class LoginForm(forms.ModelForm):
    # 创建内部类Meta
    class Meta:
        # 1. 关联的models是谁
        model = Users
        # 2. 要生成控件的属性们
        # fields = "__all__"
        fields = [
            "uname", "upwd",
        ]
        # 3. 每个控件对应的label
        labels = {
            "uname": "用户名称", "upwd": "用户密码"
        }
        widgets={
            "uname": forms.TextInput(
                attrs={"placeholder": "请输入用户名", "class": "form-control"}
            ),
            "upwd": forms.PasswordInput(
                attrs={"placeholder": "请输入密码", "class": "form-control"}
            )
        }


# class RegisterForm(forms.Form):
#     uname = forms.CharField(label="文本框")
#     upwd = forms.CharField(label="密码框", widget=forms.PasswordInput)
#     uemail = forms.EmailField(label="邮件框", required=False)
#     uage = forms.IntegerField(label="数值框", max_value=120, min_value=0)

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"
        labels = {
            "uname": "用户名称",
            "upwd": "用户密码",
            "uemail": "用户邮箱",
            "uage": "用户年龄",
        }
