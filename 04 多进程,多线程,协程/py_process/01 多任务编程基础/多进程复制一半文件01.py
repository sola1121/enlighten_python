#!/usr/bin/env python3

import os, sys
from multiprocessing import Process


if len(sys.argv) != 2:
    raise Exception("Error With Arguments")


def cut_file(root, filename, choice=1):
    file = str(root) + str(filename)
    with open(file, 'rb') as bin_file:
        bin_file = bin_file.read()
        cut_point = len(bin_file) // 2 + 1
        if choice == 1:
            cp_new1 = bin_file[:cut_point]
            with open(root + "new1", 'wb') as new1:
                new1.write(cp_new1)
        elif choice == 2:
            cp_new2 = bin_file[cut_point:]
            with open(root + "new2", 'wb') as new2:
                new2.write(cp_new2)


def cut_file2(root, filename, choice=1):
    file = str(root) + str(filename)
    size = os.path.getsize(file)
    n = size // 2
    source = open(file, 'rb')
    if choice == 1:
        new1 = open("new1", 'wb')
        while True:
            if n < 64:
                data = source.read(n)
                new1.write(data)
                break
            data = source.read(64)
            n -= 64
        source.close()
        new1.close()
        return
    elif choice == 2:
        new2 = open("new2", 'wb')
        source.seek(n, 0)
        while True:
            data = source.read(64)
            if not data:
                break
            new2.write(data)
        new2.close()
        source.close()
        return 


if __name__ == "__main__":

    root = os.getcwd() + "/"

    filename = sys.argv[1]

    p1 = Process(target=cut_file, args=(root, filename, 1))
    p2 = Process(target=cut_file, args=(root, filename, 2))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
