lauguages=['python','js','html']# checking the data type
print(type(lauguages))

names=["shella",90,"True"]
print(type(names))

thislist=list(("apple","banana","cherry"))#creating a list using the list() constructor.#note the double brackets.
print(thislist)

#indexing
names= ["anita","deborah","glad","vicky","joyce"]#accessing an item in a list.
print(names[2:4])
print(names[::-1])#reversing
print(names[-1])#negative indexing
print(names[::2])#access anita,glad joyce(using steps)
print(names[:-2])#access the first three names using negative indexing.
print(names[0:3])

x=[73,93,70,65,80]#replace or change 70 to 10
x[2]=10
print(x)

m=[70,80,89]#changing the last two values. 80 and 89
m[1:]=91,92
print(m)
m[1:3]=40,30#another method
print(m)

#inserting items. question.
#insert "watermelon" as the third item
thislist=['apple','banana','cherry']
thislist.insert(2,"watermelon")
print(thislist)

#add an item to the list
names=[10,20,30,40]
names.append(50)
print(names)

#removing list items
numbers=[10,20,30,40,50]
numbers.remove(30)#method 1
print(numbers)
numbers.pop(2)#method 2
print(numbers)
numbers.pop()#will remove the last item
print(numbers)
del numbers[1]#will remove the second item
print(numbers)

#empting the list
numbers.clear()
print(numbers)

#sorting a list
name=["anita","princess","chloe"]
name.sort()
print(name)


