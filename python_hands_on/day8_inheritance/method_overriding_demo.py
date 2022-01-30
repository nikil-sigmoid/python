class B:
    def month(self):
        print("July")


class A(B):

    def year(self):
        print("2021")

    # method overriding
    def month(self):
        print("August")

    def week(self):
        print("It is first week of July")

        # to call the method in parent class
        super().month()  # or B.month(self)


a = A()
a.year()

# If month() is not present in A class, then month() from B(parent) class will be called
a.month()
a.week()
print()

# To call the method in parent class
super(type(a), a).month()
b = B()
b.month()