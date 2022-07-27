#question1
x=8
y=2
print(x,y)#display x and y
print(x*y)#multiple of x and y
print(x**y)#exponential of x and y
print(x/y)# division
print(x//y)#float division
print(x/0)

#question2a#  write a python code prompting the user of his or her name.
name=input("enter name here:")
print(name)

#question2b
name="Anita"
telephone="0775307028"
adress="kisasi"
print("name:{}\naddress:{}\n telephone:{}".format(name,adress,telephone))

#question3a
name=input("enter name here:")#should output a sentence having the users name and age.
age=input("enter age here:")

age=int(age)
print("my name is {} and i am {} years old".format(name,age))

#3b #calculating year of birth of the above user.
current_year=2022
year_of_birth= current_year-age
print(year_of_birth)

#question 4
radius=input("enter radius here:")
area_of_a_circle= 3.14*float(radius) **2
print(area_of_a_circle)

#number
print("string" in  "substring")
print("string" not in "substring")

#s="welcome to my blog"
print(s[-2:])
print(s[-10:-2:2])

#given
str1="james"
str2=(str1[0:5:2])
print(str2)

#given
s1="Ault"
s2="kelly"
print(s1[0:2]+s2+s1[2:])

#convert into lowercase from user input
gender=input("enter gender here:")
print(gender.lower())

#list=[1,2,3,4,5,6,7,8,9,10]#printing the sum of the list
y=0
for x in list:#using the for loop. 
    y=y+x
print(y)#mind the indetation

#samplelist=["red", "green","white","black","pink","yellow"]
#samplelist.remove("red")
#print(samplelist)

#samplelist.pop(3)
#print(samplelist)
#samplelist.pop(3)
#print(samplelist)


#lists
#qn1 list1=[100,200,300,400,500]#Reverse
#list1.reverse()#mthd 1
#list1.sort(reverse = True)#mthd 2
#print(list1[::-1])#mthd 3

#qn2
list1=["m","na","i""k"]#joining the two lists
list2=["y","me","s""lly"]







