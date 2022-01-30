class B:
    def day(self):
        print("Today is Friday. Yay!!!")


class A(B):
    def month(self):
        print("July")


a = A()
a.day()
a.month()