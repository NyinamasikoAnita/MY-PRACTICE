#num1. print the first ten natural numbers using the while loop

#i = 1
#while i <= 10:
   # print(i)
   # i += 1

 #num2.
#num=int(input("enter number here:"))
#sum=0
#for num in range(1,num+1,1):
  #  sum = sum+num
#print("the sum of the first 10 numbers is",sum)

#functions
#num1
def my_func(name,age):

    print("name:anita")
    print("age:26")
my_func("anita", 26)

#num2 call functions with 3 and 2 arguments
def func1(*numbers):
    for i in numbers:
        print(i)

func1(20,40,60)
func1(80,100)


#num3
def calculation(a,b):
    addition=a+b
    subtraction=a-b
    return(a+b,a-b)
result=calculation(40,10)
print(result)



#num4
def showEmployee(name,salary=9000):
    print(name+ ":",salary)

showEmployee("ben",12000)
showEmployee("jessa")

#num5# nested function
def func1(a,b):

    #inner function
    def addition(a,b):
        return a+b

        #call inner function from outer function
    x=addition(a,b)
    return x+5

result=func1(1,1)
print(result)


#num6
def addition(num):
    if num:
        #call same function by reducing number by 1
        return num + addition(num -   1)
    else:
        return 0
result = addition(10)
print(result)






    





    

