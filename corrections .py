#reverse the tuple question 1 corrections for assignment.
tuple=(10,20,30,40,50)
print(tuple[::-1])

#question 2. print the value 20
tuple1=("orange",[10,20,30],(5,15,25))
y=tuple1[1]
print(y[1])

#question 3. copy elements (44,55)
tuple=(11,22,33,44,55,66)
tuple1=tuple[3:5]
print(tuple1)

#question #change 22 into 222.  
tuple1=(11,[22,33],44,55)
tuple1[1][0]=222
print(tuple1)

#sets 
#question1 update the first set with items that exist in the first set not in the second set.
set1={10,20,30}
set2={20,40,50}
set3=set1.difference_update(set2)
print(set1)

#question2 return a set of elements present in set 1 or 2. but not both
set1={10,20,30,40,50}
set2={30,40,50,60,70}
set1.symmetric_difference_update(set2)
print(set1)

#question3 
set1={10,20,30,40,50}
set2={60,70,80,90,10}
if set1.isdisjoint(set2):
    print("have nothing in common")
else:
 print("two sets have items in common")
 print(set1.intersection(set2))

 #dictionaries.convert the two lists into a dictionary.
 #question 1
 keys=["ten","twenty","thirty"]
 values=[10,20,30]
 dict1=dict(zip(keys,values))#zip function pairs list items with other list items
 print(dict1)

 #question 2
 #merging two python dictionaries into 1
 dict1={"fouty":40,"ten":10}
 dict2={"fifty":50,"sixty":60}
 dict3=dict1|dict2 #this function merges two dictionaries or union
 print(dict3)

 #question 3



    
    


      

    
    



