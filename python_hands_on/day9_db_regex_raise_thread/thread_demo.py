from threading import Thread
from time import sleep


class Hello(Thread):

    def run(self):
        for i in range(0, 20):
            print("Hello")
            sleep(1)


class Hi(Thread):

    def run(self):
        for i in range(20):
            print("Hi")
            sleep(1)


t1 = Hello()
t2 = Hi()

# Thread-1
t1.start()

# Thread-2
sleep(0.2)
t2.start()

t1.join()
t2.join()

# Controlled by main thread
print("Good bye everyone! Thanks for your patience.")
