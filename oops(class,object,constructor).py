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


#Inheritance
class Vehicle:
    def data(self):
        print("Vehicle Type : car,bus,two wheeler, three wheeler, etc..,")

class Car(Vehicle):
    brand = "Tata"
    model = "Punch"
    color = "Blue"

#v = Vehicle()
#v.data()
# c = Car()
# c.data()
# print(c.brand,c.model,c.color)

#Multi level inheritance
#1.power
#2.telephone -> call,power
#3.phone -> power,call,songs
#4.smartphone -> power,call,songs,internet

class power:
    name = "tesla"
    def fun1(self):
        print("Read to supply the power")
class telephone(power):
    def fun2(self):
        print("Read to talk with your network")
class phone(telephone):
    def fun3(self):
        print("Read to talk with friends and play the songs")
class smartphone(phone):
    def fun4(self):
        print("Explore your profile in Internet")

s = smartphone()
# s.fun4()
# s.fun3()
# s.fun2()
# s.fun1()
# print(s.name)

#Hierachical Inheritance
class Upi:
    def money_tranfer(self):
        print("Money Transfer Logic")

class Gpay(Upi):
    def gpy_tranfer_request(self):
        print("Gpay money transfer request activate")

class paytm(Upi):
    def paytm_tranfer_request(self):
        print("paytm money transfer request activate")


# g = Gpay()
# g.gpy_tranfer_request()
# g.money_tranfer()
# p = paytm()
# p.paytm_tranfer_request()
# p.money_tranfer()


#Multiple Inheritance

class Camera:
    def capture(self):
        print("Take Beautiful Pictures..")

class Radio:
    def speacker(self):
        print("Enjoy with super songs")

class Mobile(Camera,Radio):
    def all_access(self):
        print("Explore the world with your mobile")

m = Mobile()
m.all_access()
m.capture()
m.speacker()



#compile time polymorphism/method overloading
"""
#Single Class with single named functions
#but we pass diffrent arguments in functions
"""
class cal:
    def add(self,a=None,b=None,c=None,d=None):
        if a!=None and b!=None and c!=None and d!=None:
            print("Adding in 4 args ",a+b+c+d)
        elif a!=None and b!=None and c!=None:
            print("Adding in 3 args ",a+b+c)
        elif a!=None and b!=None:
            print("Adding in 2 args ",a+b)
        else:
            print("1 args ",a)
c = cal()
# c.add(1,2,3)
# c.add(1,2)
# c.add(1)
# c.add(1,2,3,5)


class telephone:
    def call(self):
        print("Talk with friends in wired connection")

class phone(telephone):
    def call(self):
        super().call()
        print("Talk with friends in wireless connection")

class smartphone(phone):
    def call(self):
        super().call()
        print("Talk with  your friends video call")

sm = smartphone()
# sm.call()


#Operator overloading
a = 10
b = 3
#integers ->ADD
#string -> concadinate
#print(a+"y")
print(a.__add__("d"))
print(a.__sub__("d"))
print(a.__sub__(3))
print(a.__mul__(4))
print(a.__mul__("o"))



