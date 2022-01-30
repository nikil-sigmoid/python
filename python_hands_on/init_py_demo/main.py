# Two main reasons we use __init__.py
# 1) When we import some package, its __init__.py file will execute automatically, so we can import everything in that file, so that we don't need to remember path of every module to import
# 2) If you want something to be initialized; for example, logging (which should be put in the top level)


# If we leave our __init__.py file in my_classes package blank then we'll have to access two modules in the given way:
# from my_classes.mod1 import One
# from my_classes.mod2 import Two
#
# obj_one = One()
# obj_two = Two()


# But if we specify below two lines in __init__.py of my_classes, we have to just import resouces packages, that's it and we can use all modules/classes.
# from my_classes.mod1 import One (in /my_classes/__init__.py file)
# from my_classes.mod2 import Two (in /my_classes/__init__.py file)

import my_classes

obj_one = First()
obj_two = Second()


# Reference: https://www.youtube.com/watch?v=cONc0NcKE7s