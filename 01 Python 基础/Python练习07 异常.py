# %%
# 捕获异常
try:
    num = 100
    zero = 1
    print(num/zero)
except ZeroDivisionError as ze:   # 捕获除0异常
    print(ze, "发生异常")
except:
    print("发生异常")
else:
    print("未发生异常.")
finally:
    print("整个异常捕获完成.")


# %%
# 打开文件, 捕获常见的文件打开异常
try:
    fp = open("Python练习.txt", "rb")
    while content:=fp.read(16):
        print(content)
except FileNotFoundError as err:
    print(err, "文件没有找到")
finally:
    fp.close()


# %%
# 异常的穿透
try:
    print("外层语句.")
    try:
        raise Exception("内层的异常")
    except ValueError:
        print("内层的值异常")
except Exception as err:
    print(err)
    print("捕获外层的所有异常, 包括内层try的异常")
# %%
