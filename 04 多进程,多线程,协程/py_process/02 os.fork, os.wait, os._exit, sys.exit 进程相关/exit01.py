import os, sys

# os._exit(0)   # 直接就结束进程了, 没有废话, 走得潇洒 

print("process over")

try: 
    sys.exit("散了吧散了吧, 没了没了~")   # 结束时会返回参数
except SystemExit:
    print("通过异常结束进程, 现在被捕获了")
