#oops
"""
Syntax of class
class class_name:
    #set of attributes and functions

Syntax of object
variable = class_name()
"""

# class demo:
#     name = "Stephen"
#     age = 20
#     def fun1(self):
#         print("Hello Logesh..")
#
# d = demo()
# print(d.name)
# print(d.age)
# d.fun1()


class car:
    brand = None
    model = None
    color = None
    fuel = None
    price = None
    def engine(self):
        print(self.brand,"car engine start,run,stop..")
        print("END".center(25,"*"))
# c1 = car()
# c1.brand = "TATA"
# c1.model = "Nexon"
# c1.color = "blue"
# c1.fuel = "Petrol"
# c1.price = 1500000
# print("Brand :",c1.brand)
# print("Model :",c1.model)
# print("Color :",c1.color)
# print("Fuel :",c1.fuel)
# print("Price :",c1.price)
# c1.engine()
#
# c2 = car()
# c2.brand = "Hyundai"
# c2.model = "Verna"
# c2.color = "black"
# c2.fuel = "Disel"
# c2.price = 1800000
# print("Brand :",c2.brand)
# print("Model :",c2.model)
# print("Color :",c2.color)
# print("Fuel :",c2.fuel)
# print("Price :",c2.price)
# c2.engine()

#constructor function
"""
class class_name:
    def __init__(self):
        #block of code
"""

class mobile:
    brand = None
    model = None
    color = None
    ram = None
    camera = None
    price = None
    def __init__(self,b,m,c,r,cam,p):
        self.brand = b
        self.model = m
        self.color = c
        self.ram = r
        self.camera = cam
        self.price = p

        print("Brand :",self.brand)
        print("Model :",self.model)
        print("Ram :",self.ram)
        print("Camera :",self.camera)
        print("Price :",self.price)
        print("END".center(25, "*"))


m1 = mobile("Samsung","S26","Red","12 GB","50 MP","125000")
m2 = mobile("Apple","16 Pro","Black","16 GB","108 MP","145000")





