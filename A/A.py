#3つの関数
import time

def f():
    start_time=time.time()
    for i in range (10000):
        i**10
    end_time=time.time()

    print(end_time - start_time)


def k():
    print(time.localtime)



def h():
    start_time=time.time()
    a=10
    b=10
    c=a*b
    end_time=time.time()
    print(end_time - start_time)

if __name__ =="__main__":
    f()
    k()
    h()
