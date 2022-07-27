x="mathematical computing"
print(type(x))#variable type
a="hello,world!"
print(a[1])#getting a character at position 1
print(a[0])#getting character at position 0
m = 2
print(type(m))#variable type

#indices/index
print(x[4])#getting a character position
print(x[12])

#length of a string
print(len(x))

#looping
for i in x:
  print(i)

w= "development"
for s in w:
  print(s)#looping through variable"w"

print(len(w)) #for length
print(type(w))
print("p" in w)#checking if a character is present in variable "w"
print("dev" in w)

#slicing  (with slicing you eliminate or ignore the last character)
d="develop"
print(d[1:4])
print(d[0:3])
print(d[2:5])
print(d[0:4])
print(d[3:6])
print(d[:5])

#negative indexing
g="hello"
print(g[-5:-2])
print(g[-3:-1])
print(g[-3:])
print(g[:-3])

#modifying 
print(g.upper())#for uppercase
print(g.lower())#for lowercase

#spliting
p="hello, world!" 
print(p.split(","))# forms a list


#replace
print(p.replace("h","j"))

str1=''
print(str1)



str1='hello'
str2='world'
str3=str1+str2
print(str3)

 















 