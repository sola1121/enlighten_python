import os
import hashlib
from multiprocessing import Pool, Manager


def inner_copy_file(filename, src_path, dest_path, que):
    src_path_name = src_path + "/" + filename
    dest_file_name = dest_file + "/" + filename

    with open(src_file_name, "rb") as src_file:
        with open(dest_file_name, "wb") as dest_file:
            for data in src_file:
                dest_file.write(data)

    que.put(filename)   # 向进程池队列中放入当前拷贝完成的文件名


def copy_file(filename, src_path, dest_path, que):
    if not os.path.exists(src_path):
        print("the source path %s is not exists." % src_path)
        return 
    if not os.path.exists(dest_path):
        try:
            os.makedirs(dest_path)
        except:
            print("create directory %s error." % dest_path)
            return 

    inner_copy_file(filename, src_file, dest_file, que)


def hash_code(file):
    sha1_code = hashlib.sha1()
    with open (file, 'rb') as fr:
        while True:
            data = fr.read(4096)
            if not data:
                break
            sha1_code.update(data)
    return sha1_code.hexdigest()


def exist_handle(path_name):
    count = 0
    old_path_name = path_name
    new_path_name = path_name
    while os.path.isfile(path_name) or os.path.isdir(path_name):
        count += 1
        new_path_name = old_path_name + " - 副本(%d)" % count
    else:
        return new_path_name


if __name__ == "__main__":
    src_path = input("请输入要拷贝的文件目录: ")

    all_file_names = os.listdir(src_path)
    all_num = len(all_file_names)


    po = Pool()
    que = Manager.Queue()   # 进程间通讯的队列

    # 拷贝文件操作
    for name in all_file_names:
        po.apply_async(func=copy_file, args=(name, src_path, dest_path))
        po.close()
        
        while num< all_num:
            file_name = que.get()   # 如果队列中拿不到, get会阻塞
            
            num += 1
            rate = num / all_num * 100   # 显示进度

            src_path_name = src_path + "/" + filename
            dest_file_name = dest_file + "/" + filename

            if hash_code(src_file_name) == hash_code(dest_file_name):
