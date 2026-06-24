#Tuple - immutable
"""
t = (10,True,"Python",30.23,10,(34,False),6+4j)
print(t)
print(type(t))
print(t[2])
print(t[1:5])
print(t[5][1])
#tuple build-in-functions
print(t.count(101))
print(t.index(10))

l = list(t)
print(l,type(l))
l.pop()
t = tuple(l)
print(t)

#store single value in tuple
t1 = (20,)
print(t1,type(t1))

b = 45,"Praveen",45,77.6
print(b,type(b))

#for loop using tuple datatype
for i in t:
    print(i)
"""

#set - not allow duplicate
"""
s = {20,True,4.2,20,"mukil",20}
print(s,type(s))
#set in build functions
#add
s.add("Nivetha")
print(s)
s.update([34,55,34,6,55])
print(s)

#remove
s.remove(6)
print(s)
s.discard(4.2222)
print(s)
s1 = s.copy()
print("s1 : ",s1)
s1.clear()
print(s1)
s.pop()
print(s)


#venn logic functions
a={1,2,3,4,5}
b={4,5,6,7,8}

print(a,f"\n{b}")
print(a.intersection(b))
print("a : ",a)
#a.intersection_update(b)
#print("a : ",a)

print(a.symmetric_difference(b))
print("a : ",a)
#a.symmetric_difference_update(b)
#print("a : ",a)

#print(a.union(b))

print(a.difference(b))
print(b.difference(a))
print("a : ",a)
#a.difference_update(b)
#print("a : ",a)



print(a.isdisjoint(b))

x = {5,6,7,1,2,3}
y = {1,2,3}

print(f"x = {x}\ny = {y}")
print(x.issuperset(y))
print(y.issubset(x))
print(x.issubset(y))

# for loop using set
for i in s:
    print(i)
"""

#Dictionary
#{key:value}
d = {"name":"Sampritha",
     "course":"AI Developer",
     "city":"Salem",
     "Mark":100,
     "IsStd":True}


print(d)
print(type(d))

print(d["name"])
print(d["city"])

print(d.get("course"))
print(d.keys())
print(d.values())

print(d.items())
d.pop("Mark")
print(d)
d.update({"CGPA":9.4})
print(d)

for i in d:
    print(i,":",d[i])

print("****************")
for i,j in d.items():
    print(i,":",j)





















