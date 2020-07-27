from threading import *
from time import sleep


class hello(Thread):
    def run(self):
        for i in range(8):
            print('hello')
            sleep(1)


class hi(Thread):
    def run(self):
        for i in range(8):
            print('hi')
            sleep(1)


t1 = hello()
t2 = hi()
t1.start()
sleep(.2)
t2.start()
#here 3thread working t1,t2,main
#while t1,t2 thread running main thread print bye
#but we want to print bye at the last after finish the t1,t2
#so t1,t2 finished work and after join , then we want main thread to print bye

t1.join()
t2.join()
print('bye')
