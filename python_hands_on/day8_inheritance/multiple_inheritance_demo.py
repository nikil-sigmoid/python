class B:
    def season(self):
        print("It is summer season")


class C:
    def pizza(self):
        print("Pizza is delicious")


class A(B, C):
    def week(self):
        print("It is the first week of July")


a = A()
a.season()
a.pizza()
a.week()
