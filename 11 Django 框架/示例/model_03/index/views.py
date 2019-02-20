from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db.models import F, Q

from .models import *  

# Create your views here.

def index_view(request):
    return render(request, "<h1>hello</h1>")

# 数据库增操作
def add_view(request):
    # Author.objects.create(name="kizuna_ai", age=2)

    # au_obj = Author(name="luna", age=0)
    # au_obj.save()

    dic = {"name": "siro", "age": 1}
    au_obj = Author(**dic)
    au_obj.save()

    return HttpResponse("Add OK")

def format_text(s):
    text = str()
    text += str(s.id) + "   " + str(s.name) + "   " + str(s.age) + "<br>"
    return text

# 数据库查询操作
def query_view(request):
    text = str()
    # au_lst = Author.objects.all()
    # for info in au_lst:
    #     text += str(info.name) + ", " + str(info.age) + ", " + str(info.email)+ "<br>"

    # au_lst = Author.objects.values("name", "age")
    # print(au_lst)
    # for info in au_lst:
    #     text += str(info["name"]) + "   " + str(info["age"]) + "<br>"

    # au_lst = Author.objects.values_list("name", "age")
    # print(au_lst)
    # for info in au_lst:
    #     text += str(info[0]) + "   " + str(info[1]) + "<br>"
        

    # au_lst = Author.objects.order_by("id")
    # for info in au_lst:
    #     text += format_text(info)

    # 条件取反, exclude()
    # au_lst = Author.objects.exclude(id=2)
    # print(au_lst)
    # for info in au_lst:
    #     text += format_text(info)

    return HttpResponse(text)

def author_list(request):
    au_lst = Author.objects.all()
    # locals() 生成的局部变量字典
    # {
    #   'au_lst': <QuerySet [<Author: Author object>, <Author: Author object>, <Author: Author object>]>, 
    #   'request': <WSGIRequest: GET '/author_list/'>
    # }
    return render(request, "author_list.html", locals())

def delete_veiw(request, id_num):
    # 真删除数据
    Author.objects.get(id=id_num).delete()
    au_lst = Author.objects.all()

    # 用isActive的方式来表示删除数据
    # author = Author.objects.get(id=id_num)
    # author.isActive = False
    # author.save()

    # 转发, 不推荐
    # return author_list(request)

    # 重定向, 向指定地址在发出一次请求 
    return HttpResponseRedirect("/author_list/")

def update_view(request, id_num=None):
    if request.method == "GET":
        author = Author.objects.get(id=id_num)
        return render(request, "update_author.html", locals())
    elif request.method == "POST":
        the_author = Author.objects.get(id=id_num)
        new_name = request.POST["author_name"]
        new_age = request.POST["author_age"]
        new_email = request.POST["author_email"]
        the_author.name = new_name
        the_author.age = new_age
        the_author.email = new_email
        the_author.save()
        return HttpResponseRedirect("/author_list/")

def add_num_view(request, num):
    # 对所有的age增加一个数
    Author.objects.all().update(age=F('age')+num)
    return HttpResponseRedirect("/author_list/")

def query_Q_view(request):
    Author.objects.filter(Q(id__gt=2)|Q(age__gte=4), isActive=True)
    return render(request, "author_list.html", locals())

def raw_view(request):
    sql = "select * from index_author where id>=2"
    au_lst = Author.objects.raw(sql)
    print(au_lst)
    for au in au_lst:
        print(au.name, au.age)
    return HttpResponse("<h1>success!</h1>")

def wife_author_view(request):
    # 正向查询: 通过wife找author
    # 1. 获取id为1的wife的信息
    wife = Author_Wife.objects.get(id=1)
    # 2. 再获取wife对应的Author
    author = wife.author
    dic = {"wife": wife, "author": author}        
    return render(request, "one2one.html", dic)

def author_wife_view(request):
    # 反向查询: 通过author找wife
    # 1. 获取id为9的author的信息
    author = Author.objects.get(id=9)
    # 2. 在获取author对应的wife
    wife = author.author_wife
    dic = {"author": author, "wife": wife}
    return render(request, "one2one.html", dic)


def book_publisher_view(request):
    # 1. 查询id为1的书籍信息
    book = Book.objects.get(id=1)
    # 2. 查询该书关联的出版社信息
    publisher = book.publisher
    dic = {"book": book, "publisher": publisher}
    return render(request, "one2many.html", dic)

def publisher_book_view(request):
    # 1. 查询id为1的Publisher的信息
    publisher = Publisher.objects.get(id=1)
    # 2. 查询该出版社所关联的所有图书
    books = publisher.book_set.all()
    dic = {"publisher": publisher, "books": books}
    return render(request, "one2many.html", dic)


def author_book_view(request):
    # 通过author查询其所有的book
    author = Author.objects.get(id=9)
    books = author.book.all()
    dic = {"author": author, "books": books}
    return render(request, "many2many.html", dic)

def book_author_view(request):
    # 通过Book查询其所有的author
    book = Book.objects.get(id=1)
    authors = book.author_set.all()
    dic = {"book": book, "authors": authors}
    return render(request, "many2many.html", dic)

def author_publisher_view(request):
    # 通过author查询其对应的所有publisher
    author = Author.objects.get(id=9)
    pubs= author.au_pub.all()
    dic = {"author": author, "publishers": pubs}
    return render(request, "many2many2.html", dic)

def publisher_author_view(request):
    # 通过publisher查找其中对应的author
    pub = Publisher.objects.get(id=1)
    authors = pub.author_set.all()
    dic = {"publisher": pub, "authors": authors}
    return render(request, "many2many2.html", dic)


def obj_count_view(request):
    count = Author.objects.auCount()
    return HttpResponse("Author count <strong> %d </strong>" % count)

def lt_age_view(request, age_num=4):
    infos = Author.objects.ltAge(age_num)
    return HttpResponse("<xmp>" + str(infos)+ "</xmp>")

def contain_word_view(request, word="pro"):
    infos = Book.objects.titleContain(word)
    return HttpResponse("<xmp>" + str(infos) + "</xmp>")