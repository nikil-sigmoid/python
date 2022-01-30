class D:
    def date(self):
        print("It is 2nd July")


class A(D):
    def day(self):
        print("July")


class B(D):
    def month(self):
        print("July")


class C(D):
    def year(self):
        print("2021")


a = A()
a.day()
a.date()

b = B()
b.date()
b.month()
