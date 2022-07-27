#python conditions and if statement
#the if ststement
from tokenize import Number


a=33
b=200
if "b<a":
    print(b>a)

#elif statement( a way of saying if the previous conditions were not true then try this condition)
c=33
d=33
if d>c:
   print("d>c")
elif a==b:
    print("a and b are equal")

 #the else ststement(catches anything which is not caught by the preceeding condiions)
e=200
f=33
if f>e:
    print("f is greater than e")
elif e==f:
    print("e and f are equal")
else:
    print("e is greater than f")

#the shorthand if (putting your statement on the same line with the if)
if e>f: print("e is greater than f")

#assignment
#arranging descending or ascending
list1=[1,2,3,4]
list1.sort(reverse=True)
print(list1)

#squaring
list=[1,2,3,4]
mylist=[Number*2 for numbers in list]




