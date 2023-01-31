# LIST
# -----------
# 1. Create a list of only even numbers.
# 2. Create one list of 1 to 10 numbers and create new list which contain square of the
# numbers from this number list.
# 3. Take three input numbers from the user and create list from those numbers.
# 4. Take one list of numbers and do sum of all numbers in that list without using sum
# function.
# 5. list_one = [1,2,3,4], list_two =[1,2,3,4], check that these two lists content is same of
# not.
# 6. list_one = [1,2,3,4], list_two =[1,2,3,4], check that these two lists
# addresses/references are same of not.
# 7. list1 = [100,200,100,400,500,300], reverse this list.
# 8. Reverse above list without using reverse function.
# 9. Reverse the above lists using slicing.
# 10. Concatenate two list index wise,
# Eg.l1 = [‘A’,’B’,’C’]
# l2 = [‘X’,’Y,’Z’]
# o/p: [‘AX’,’BY’,’CZ’]
# 11. Create one list of numbers from 1 to 10 and extract only last 5 numbers from that
# list.
# 12. Take a list of names and convert those all names into Upper case words.
# 13. Take list of names and count number of characters in each name and print on the
# console, name and its length.
# 14. Create one list of elements and take specific element and position of element from
# user and add that element at that position.
# 15. Take list of numbers and print on the console element and number of occurrences of
# that element in that list.
# 16. Check the start and end element of the lists are same or not.
# 17. Take the list of strings and sort in both ascending and descending order.
# 18. Take a number list and calculate sum and average of list elements.
# 19. Take a number list and count even and odd numbers in that list.
# 20. Reverse a list without using inbuilt function.
# 21. Get only unique elements from the list.
# 22. Take two lists with same number of elements and subtract elements from one list
# from other list element and create new list for that subtraction result.
# 23. Take one list elements and create two separate lists those contain odd numbers and
# even numbers separately.
# 24. Take a list of numbers in the string format, convert those numbers into integer
# format and get sum of all those list elements.


#Answer 1:
Even_No=[]
data=int(input("Please Enter Till How Long : "))
for x in range(data):
    if x%2==0:
        Even_No.append(x)
print(Even_No)

#Answer 2:
data=int(input("Please Enter Till How Long : "))
newSQ_list=[]
for x in range(data):
    newSQ_list.append((x*x))
print(f"From 0 to {data}, Square is of each no : {newSQ_list}")

#Answer 3:
data1=int(input("Please Enter input1 : "))
data2=int(input("Please Enter input2 : "))
data3=int(input("Please Enter input3 : "))
No1_list=[x for x in range(data1) ]
No2_list=[x for x in range(data2) ]
No3_list=[x for x in range(data3) ]

print(No1_list)
print(No2_list)
print(No3_list)

#Answer 4:

data143=int(input("Please Enter Till How Long : "))
c=0
for x in range(1,data143+1):
    c+=x
print("sum of all digits is : ",c)

#Answer 5:

list1=list(input("enter ur list1 data : "))
list2=list(input("enter ur list2 data : "))
if list1 == list2:
    print("DATA EQUAL")
else:
    print("DATA NOT EQUAL")

#Answer 6:

list1=list(input("enter ur list1 data : "))
list2=list(input("enter ur list2 data : "))
if list1 is list2:
    print("DATA reference EQUAL")
else:
    print("DATA reference NOT EQUAL")

#Answer 7:
list143= [100,200,100,400,500,300]
reverse=list143[::-1]
print("Reversed of list is : ",reverse)

#Answer 8:
l1=len(list143)
reverse1=[]
l2=len(reverse1)
print(l1,l2)

while l2<l1:
    reverse1.append(list143[3])
    # list143.pop()
print(reverse1)
print(l1,l2)


#Answer 9:

a=list143[::-1]
print("Reverse of a list using slicing : ",a)

#Answer 10:

v1143=list(input("enter any string1 : "))
v2143=list(input("enter any string2 : "))
new143=[]
for x in range(len(v2143)):
    if len(v2143)==len(v1143):
        new143.append((v1143[x]+v2143[x]))
    else:
        print("Please Enter Same Length")
print("Concatenate two list index wise is : ",new143)

#Answer 11:

list_created=int(input("Enter a value to fetch last 5 digits : "))
new_L123=[x for x in range(list_created)]
print("Last 5 digits are : ",new_L123[:list_created-6:-1])

#Answer 12:
def operation():
    print("Mini UpperCase Converter ON ")
    n=(input("Perform Operation Y or N : "))
    if n=='Y' or n=='y':
        List24354=input("Enter any word to convert to upperCase : ").upper()
        print(List24354)
        v=input("TO Use Again press 'Y' or 'N' : ")
        if v=='Y' or v=='y':
            operation()
        else:
            print("ThankYou !!")
operation()
        
#Answer 13:

list_of_name=["naveen","raja","venky","chakri","deva"]
for x in list_of_name:
    print("number of characters in '{}' is : {}".format(x,len(x)))
        
#Answer 14:
list_of_name1=["naveen","raja","venky","chakri","deva"]
print("List Of Name are : ",list_of_name1)
new_list324=["naveen","raja","venky","chakri","deva"]
for x in list_of_name1:
    print(f"please select the position of {x} in : ",end='')
    v2435=int(input())
    new_list324[v2435-1]=x
print("Final List is : ",new_list324)

#Answer 15:
list_of_no=[1,23,44,54,2,12,4,43,5,64,4,3,3,4,53]
print("List Of Numbers are : ",list_of_no)
for x in list_of_no:
    print("Number is '{}' and no of time repeated is {}".format(x,list_of_no.count(x)))

#Answer 16:
list_of_no2=['naveen',1,23,44,54,2,12,4,43,5,64,4,3,3,4,53,1,'naveen']
len122=len(list_of_no2)
if list_of_no2[0]==list_of_no2[len122-1]:
    print("Element Same")
else :
    print("Not Same ")

#Answer 17:
list_of_no234=[1,23,44,54,2,12,4,43,5,64,4,3,3,4,53]
list_of_no234.sort()
print("Ascending Order is : ",list_of_no234)
print("Decending Order is : ",list_of_no234[::-1])

#Answer 18:
list_of_no23544=[1,23,44,54,2,12,4,43,5,64,4,3,3,4,53]
print("sum of list of element is : ",sum(list_of_no23544))
print("Average of the List is : ",sum(list_of_no23544)/len(list_of_no23544))

#Answer 19:
list_of_no544=[1,23,44,54,2,12,4,43,5,64,4,3,3,4,53]
Even_No=0
Odd_No=0
for x in list_of_no544:
    if x%2==0:
        Even_No+=x
    else :
        Odd_No+=x
print(f"Sum of Even_No are : '{Even_No}' and Sum of ODD_No are : '{Odd_No}'")

#Answer 20:
list_of_no54400=[1,23,44,54,2,12,4,43,5,64,4,3,3,4,53]
Reversed=[]

for x in range(1,len(list_of_no54400)+1):
    Reversed.append(list_of_no54400[len(list_of_no54400)-x])
print(Reversed)

#Answer 21:

list_of_no5440aa0=[1,23,44,54,2,12,4,43,5,64,4,3,3,4,53]
unique_no=[]
for x in list_of_no5440aa0:
    if list_of_no5440aa0.count(x) ==1:
        unique_no.append(x)
print("Unique_numbers are : ",unique_no)

#Answer 22:
v1143345=[1,23,44,54,2,12,4,43,5,64,4,3,3,4,53]
v2143456=[1,23,44,54,2,12,4,43,5,64,4,3,3,4,53]
new143456=[]
for x in range(len(v1143345)):
    if len(v1143345)==len(v2143456):
        new143456.append((v1143345[x]+v2143456[x]))
    else:
        print("Please Enter Same Length")
print("Addition two list index wise is : ",new143456)


#Answer 23:
list_of_no5423244=[1,23,44,54,2,12,4,43,5,64,4,3,3,4,53]
Even_No213=[]
Odd_No213=[]
for x in list_of_no5423244:
    if x%2==0:
        Even_No213.append(x)
    else :
        Odd_No213.append(x)
print("Even_Numbers are : ", Even_No213)
print("Odd_Numbers are : ", Odd_No213)

#Answer 24:

list_of_no4232=['22','34','44','55','663']
out_put_1=[]
for x in list_of_no4232:
    out_put_1.append(int(x))
print("Convert str list to int list is : ",out_put_1)
print("SUM of List is : ",sum(out_put_1))
