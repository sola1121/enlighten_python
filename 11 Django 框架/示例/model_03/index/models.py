from django.db import models

# 声明自定义的objects - models.Manager
class AuthorManager(models.Manager):
    # 添加自定义函数 - 查询Author表中共有多少条数据
    def auCount(self):
        return self.all().count()

    def ltAge(self, age_num):
        if age_num < 0:
            age_num = 1
        elif age_num > 100:
            age_num = 100
        return self.filter(age__lt=age_num)


class BookManager(models.Manager):
    def titleContain(self, word):
        return self.filter(title__contains=word)


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=15)
    website = models.URLField(max_length=200)
    def __str__(self):
        return self.name

    class Meta:
        db_table = "publisher"
        verbose_name = "出版社"
        verbose_name_plural = verbose_name


# 书籍; title 书名, publicate_date 出版时间
class Book(models.Model):

    objects = BookManager()

    title = models.CharField(max_length=50)
    publicate_date = models.DateField()
    publisher = models.ForeignKey(Publisher, null=True)
    def __str__(self):
        return self.title

    class Meta:
        db_table = "book"
        verbose_name = "书籍"
        verbose_name_plural = verbose_name
        ordering = ["-publicate_date"]


# 作者; name 名字, age 年龄, email 邮箱, 可以为空, 用户是否启用 默认为True启用
class Author(models.Model):
    # 使用AuthorManager覆盖当前的objects
    objects = AuthorManager()

    name = models.CharField(max_length=30) 
    age = models.IntegerField()
    email = models.EmailField(null=True)
    isActive = models.BooleanField(default= True)
    # 增加一个对Book的多对多引用
    book = models.ManyToManyField(Book)
    # 增加一个对Publisher的多对多引用 
    au_pub = models.ManyToManyField(Publisher)

    def __str__(self):
        return self.name
    # 声明内部类, 来定义当前类在管理页面中的展现形式
    class Meta:
        # 1. 自定义当前表的名字 Author
        db_table="author"
        # 2. 修改实体类在后台管理页中的名称(单数)
        verbose_name = "作者"
        # 3. 修改实体类在后台管理页中的名称
        verbose_name_plural = verbose_name
        # 4. 首先按照年龄将序排列, 其次按照ID升序排列
        ordering = ["-age", "id"]


class Author_Wife(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    # 增加一对一引用, 引用自author实体
    author = models.OneToOneField(Author, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "author_wife"
        verbose_name = "夫人"
        verbose_name_plural = verbose_name