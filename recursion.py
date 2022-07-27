from unittest import result


def fact(n):

   if n==0:
       return 1
   return n*fact(n-1)

result = fact(5)
print(result)


#use recursive function to calculate the sum of numbers 1-10

