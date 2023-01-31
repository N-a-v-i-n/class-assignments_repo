# ##Dictionary
# 1. Create an empty dictionary then add some key value pairs, like
# name,age,address..etc.
# 2. Take two lists of same size and make first list members as key and second list
# elements as values.
# 3. Take one lists of duplicate numbers, and make a dictionary which key is list element
# and value is number of occurrences of that element in that list.
# 4. Write a Python script to add a key to a dictionary.
# 5. Write a Python program to iterate over dictionaries using for loops.
# 6. Write a program to sum values in that dictionary.
# 7. Write a Python program to sort a given dictionary by key.
# 8. Write a Python program to sort a given dictionary by values.
# 9. Write a Python program to get the maximum and minimum values of a dictionary.
# 10. Write a Python program to get total number of items in that dictionary.
# 11. Write a Python program to replace values of dictionary with sum of key and value.
# 12. Write a Python program, take on list of words and create new dictionary its words
# are keys of that dictionary and values as length of the word.
# 13. Write a Python program to invert key, value pairs in dictionary.
# 14. Write a Python program, take one numbers list and create new dictionary its key is
# number and value is square of that number from numbers list.
# 15. Merge two dictionaries into one dictionary.
# 16. Write a Python program to sum all the dictionary values without using sum function.
# 17. Write a Python program to transform a dictionary into a list of tuples.
# 18. Write a python program to find size of dictionary.
# 19. Create dictionary with key value pairs and then change value of particular key.
# 20. Write a program, user will enter its details like name, age ..etc , create one dictionary
# for that and display readable information on the console of that user.

#Answer 1:
dir133={}
for x in range(2):
    dir133[input("Please enter any key to add into dictionary : ")]=input("Please enter any value to add into dictionary : ")
print(dir133)

#Answer 2:
list123=["A","B","C","D"]
list1231=[466,467,468,469]
em_dict13={}
for x in range(len(list123)):
    em_dict13[list123[x]]=list1231[x]
print(em_dict13)

#Answer 3:


#Answer 4:
dir133133={}
for x in range(1):
    dir133133[input("Please enter any key to add into dictionary : ")]=''
    print(f"The Key is Added ")
print(dir133133)

#Answer 5:
dic21342={'name': ['naveen'], 'age': ['25']}
for x,y in dic21342.items():
    print(f"The key is : '{x}' and its value is : {y}")


#Answer 6:
dic5443={"a":25,"b":26,"c":27}
sum_of_val=0
for x in dic5443.values():
    sum_of_val+=x
print("Total sum of Values in Dictionary is : ",sum_of_val)

#Answer 7:
dic5443={"c":25,"a":26,"b":27}
temp=[]
for x,y in dic5443.items():
    temp.append([x,y])
temp.sort()
print("After sorting : ",dict(temp))

#Answer 8:

dic544378={"c":25,"a":26,"b":27}
temp=[]
for x,y in dic544378.items():
    temp.append([y,x])
temp.sort()
print("After sorting : ",dict(temp))

#Answer 9:

dic5443778={"c":25,"a":26,"b":27}
minim=min(dic5443778.values())
maxi=max(dic5443778.values())
print("Minimun value is : ",minim)
print("max value is : ",maxi)


#Answer 10:

dic5448883={"a":25,"b":26,"c":27}
sum_of_val=0
for x in dic5448883.items():
    sum_of_val+=1
print("Total no of Values/keys in Dictionary is : ",sum_of_val)


#Answer 11:
dic5448j3={46:25,78:26,87:27}
for x,y in dic5448j3.items():
    c=x+y
    dic5448j3[x]=c
print(dic5448j3)

#Answer 12:
dict245313={}
list342=["Naveen","Vishnu","Johnson","Shibani","Rohan"]
for x in list342:
    dict245313[x]=len(x)
print(dict245313)

#Answer 13:
dict4284={'Naveen': 6,'Vishnu': 12, 'Johnson': 14, 'Shibani': 7, 'Rohan': 5}
inverted_dic={}
for x,y in dict4284.items():
    inverted_dic[y]=x
print("after inverted duplicate key are deleted : ",inverted_dic)

#Answer 14:
temp_list=[1,2,435,64,45,6,3,5]
temp_dict={}
for x in temp_list:
    temp_dict[x]=x*x
print(temp_dict)

#Answer 15:
dict11={"c":25,"a":26,"b":27}
dict22={46:25,78:26,87:27}
for x,y in dict22.items():
    dict11[x]=y
print(dict11)

#Answer 16:
dict1212={"c":25,"a":26,"b":27}
sum=0
for x in dict1212.values():
    sum+=x
print(sum)
    
#Answer 17:
dict12112={"c":25,"a":26,"b":27}
t_lsit=[]
for x,y in dict12112.items():
    t_lsit.append((x,y))  
print(tuple(t_lsit))
print(t_lsit)

#Answer 18:
import sys
dict12pp={"c":25,"a":26,"b":27}
print("sizeOfDict : ",sys.getsizeof(dict12pp) )

#Answer 19:
ict12112={"c":25,"a":26,"b":27}
for x,y in ict12112.items():
    ict12112[x]=466
print(ict12112)

#Answer 20:
dictemp={"Name":'',"Age":'',"Likes":''}
for x,y in dictemp.items():
    print(f"Please enter {x} : ",end='')
    dictemp[x]=input()
print(dictemp)
