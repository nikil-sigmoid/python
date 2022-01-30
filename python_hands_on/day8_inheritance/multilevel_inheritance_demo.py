class D:
    def date(self):
        print("It is 2nd July")


class C(D):
    def day(self):
        print("Friday")


class B(C):
    def month(self):
        print("July")


class A(B):
    def year(self):
        print("2021")


a = A()
a.year()
a.month()
a.day()
a.date()