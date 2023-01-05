# Module 2 Part-1 Assignment
# 1. Take name and age of the person from input and display on the console using format specifier.
# 2. Take name and age of the person from input and display on the console using fstring.
# 3. Take name and age of the person from input and display on the console using format method.
# 4. Take whole number, floating point number, string, Boolean data. Check each of those data type.
# 5. Take input any string and extract some part of the string.

# #1:-
name =input("Enter Your Name : ")
age =input("How Old Are You : ")
print("Printing using format specifier")
print("Haii %s !!, Please Confirm Your Age is '%s' "%(name,age))  #Print using format specifier

# #2:-
print()
print("Printing using fstring")
print(f"Haii {name} !!, Please Confirm Your Age is '{age}' ")  #Print using fstring

# #3:-
print()
print("Printing using format method")
print("Haii {} !!, Please Confirm Your Age is '{}' ".format(name,age))  #Print using format specifier
# print("Haii {name1} !!, Please confirm Your Age is '{age1}'".format(name1=input("Enter Your Name : "),age1=input("How Old Are You : ")))   #Print using format specifiers

#4:-

roll_num=int(input("College_roll-no : "))
name_str=str(input("Name : "))
percentage=float(input("Percentage on final-Year : "))
result=percentage>=35

print("Printing DataTypes")
print()
print(f"dataType for Roll no is : {type(roll_num)}")
print(f"dataType for Percentage is : {type(percentage)}")
print(f"dataType for Name's is :  {type(name_str)}")
print(f"dataType for Results is : {type(result)}")

#5:-
print()
print("Take input any string and extract some part of the string")
full_name = input("Enter full name as per PAN : ")
store_ref=[]
last_name=""
count=0
count1=1
for x in range(len(full_name)):
    if (full_name[x]!=" " and count==0):
        store_ref.append(full_name[x])
        

        
    elif (full_name[x]==" "):
        next_index_count=x
        last_name= full_name[next_index_count::1]
        count+=1

first_name=full_name[:len(store_ref):1]

print(f"firstName : {first_name}" ) 
print(f"lastName : {last_name}")

