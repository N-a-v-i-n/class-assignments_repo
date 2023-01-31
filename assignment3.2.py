# #Tuple:
# -------------
# 1. Create tuple of numbers 1 to 10.
# 2. Create single value tuple.
# 3. Create one number element tuple and square all the elements in that tuple and
# store in new list.
# 4. Write a Python program to create a tuple.
# 5. Write a Python program to create a tuple with different data types.
# 6. Write a Python program to create a tuple of numbers and print 2nd item.
# 7. Write a Python program to unpack a tuple into several variables.
# 8. Write a Python program to add an item to a tuple.
# 9. Write a Python program to convert a list to a tuple.
# 10. Write a Python program to find the length of a tuple without using len function.
# 11. Write a Python program to reverse a tuple.
# 12. Write a Python program to convert a list of tuples into a dictionary.
# 13. Write a Python program to calculate the product, multiplying all the numbers in a
# given tuple.
# 14. Write a Python program to calculate the average value of the numbers in a given
# tuple.
# 15. Write a Python program to convert a tuple of string values to a tuple of integer
# values.
# 16. Write a Python program to convert a given list of tuples to a list of lists.
# 17. Write a python program to get size of tuple.
# 18. Create one and list and one tuple with same elements and compare their sizes.
# 19. Get count a particular element in tuple.
# 20. Write a Python program to get the 4th element and 4th element from last of a tuple.

# #Answer 1:
temp2324=[]
for x in range(1,11):
    temp2324.append(x)
print("Tuple_Number are : ",tuple(temp2324))

#Answer 2:
single_value_tuple=(1)
print(type(single_value_tuple))
print("single_value_tuple : ", single_value_tuple)

#Answer 3:
value_tuple24=(1,334,54,66,57,75,34,435)
new_list324=[]
for x in value_tuple24:
    new_list324.append((x*x))
print("Square of each Tuple Elements are : ",new_list324)

##Answer 4:
tuple1234 = (1, 2, 3)
print("Tuple Vlaue are : ", tuple1234)

##Answer 5:
tuple48724 = (1, "Hello", 3.4)
print("Tuple Vlaue With Mixed DataType are ",tuple48724)

#Answer 6:
empty_li=[]
for x in range(10):
    empty_li.append(x)
empty_tuple=tuple(empty_li)
print("Second Value in tuple is : ",empty_tuple[1])

#Answer 7:
tuple3453=(1,2,4,5,6)
t1,t2,t3,t4,t5=tuple3453
print(t1,t2,t3,t4,t5)

#Answer 8:


#Answer 9:

list984734=[4,6,8,2,"navii"]
print("Converted List into tuple : ",tuple(list984734))

#Answer 10:
tuple872=(4,6,8,2,"navii")
c428=0
for x in tuple872:
    c428+=1
print(c428)

#Answer 11:
tuple8w72=(4,6,8,2,"navii")
reverse_tuple=tuple(tuple8w72[::-1])
print(reverse_tuple)

#Answer 12:
list_of_tuple=[('A',1),("B",2),('c',3)]
final_dict={}
final_dict=dict(list_of_tuple)
print(final_dict)

#Answer 13:
tuple842=(1,324,53,56,5)
product35=1
for x in tuple842:
    product35*=x
print(product35)

#Answer 14:

tuple842=(1,324,53,56,5)
sum312=sum(tuple842)
avg312=sum312/len(tuple842)
print(avg312)

#Answer 15:
tuple842312=("1","43","431")
list_int=[]
for x in tuple842312:
    list_int.append(int(x))
print(tuple(list_int))

#Answer 16:
list_of_tuple3123=[('A',1)]
list_of_list12=[]
for x in list_of_tuple3123:
    list_of_list12.append(list(x))
print(list_of_list12)

#Answer 17:
import sys
tuple13234=(2,34,23,42,32)
print("Size of Tuple is : ",sys.getsizeof(tuple13234))

#Answer 18:
tuple83478=(2,34,23,42,32)
list838264=[2,34,23,42,32]
print("Size of Tuple is : ",sys.getsizeof(tuple83478))
print("Size of List is : ",sys.getsizeof(list838264))

#Answer 19:
tuple83478=(2,34,23,42,324,4,4,32,23,23,)
for x in tuple83478:
    print(f"The Count of '{x}' is : {tuple83478.count(x)}")

#Answer 20:
tuple8338=(2,34,23,42,324,4,4,32,23,23,11,12)
l8338=len(tuple8338)-1
print("The 4th Element in a tuple is : ",tuple8338[4])
print("The Last 4th Element in a tuple is : ",tuple8338[l8338-3])



