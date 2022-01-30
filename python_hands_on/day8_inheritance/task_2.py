class FlyingMachine:

    def travel(self):
        print("Machines which fly are used to travel from one point to another")


class Aeroplane(FlyingMachine):

    def fly(self):
        print("Aeroplane flies at 800 mph!")

    def travel(self):
        print("Aeroplanes help us travel faster")


class Helicopter(FlyingMachine):

    def hover(self):
        print("Helicopter can hover over ground")


helicopter = Helicopter()
helicopter.hover()
helicopter.travel()