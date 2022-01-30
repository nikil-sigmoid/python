import car
car.print_fav_car()
print()

from car import print_fav_car
print_fav_car()
print()

from car import print_fav_car as pfc
pfc()
print()

import car as c
c.print_fav_car()
print()

from car import *
print_fav_car()
print()

