import os, sys, time

pid = os.fork()

if pid < 0:
    print("New process fialed.")
elif pid == 0:
    print("New process created.")
    sys.exit("Exit child process.")
elif pid > 0:
    print("Parent process.")
    while True:
        pass
