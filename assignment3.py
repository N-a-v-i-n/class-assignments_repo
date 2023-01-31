#String
#-----------------
# 1. Display three strings ‘Name’,’Is’ ,’James’ as ‘ Name**Is**James’.
# 2. Accept two numbers input from user, and do mathematical operations, (addition,
# subtraction, multiplication, division, modulo division, floor division).
# 3. Convert decimal number into octal number using , format specifier in print function.
# 4. Display float number with two decimal places, using print function.
# 5. Take three different strings from input and assign to three different variables and
# display on the console.
# 6. Take a input trinsg and convert each character into upper case.
# 7. Take input string and calculate its length without using len function.
# 8. Take input string and extract only even position characters.
# 9. Take circle radius input from user and calculate area of a circle.
# 10. Reverse a string by its words.
# 11. Take input string from user and check that is entered string is palindrome or not.
# 12. Take one input string and find ASCII value of each character and print on the console
# with that character.
# 13. Ask user to enter number from 0 to 255 and print on the console its corresponding
# character.
# 14. Get word count , from paragraph.
# 15. Take input string from user, while entering string if user gives spaces at starting or
# ending of the string, remove those spaces and print string on the console.
# 16. Reverse the entered 4-digit number. Eg. input is 1804, o/p should be: 4081.
# 17. Take two string and add alphabets alternatively and form single string.eg.st1 = “BAT”
# ,st2=”GIT”, then output should be: BGAITT.
# 18. Count number of vowels in the string.
# 19. Remove any special symbol, numbers from the list, keep only alphabets.
# 20. Take two input strings from the user and check are those strings same or not.
# 21. Write a program to get size of string.

# Answer 1:
f1='Name'
f2='Is'
f3='Naveen'
print(f1,f2,f3,sep='**')

#Answer 2:
def operation():
    print("Mini Calculator ON ")
    n=(input("Perform Operation Y or N : "))
    if n=='Y' or n=='y':
        n1=int(input("Enter First_No : "))
        n2=int(input("Enter Second_No : "))
        Please_select_operation=[["add",1],["sub",2], ["multiple",3], ["division",4], ["modulo_division",5], ["floor_division",6]]
        print("Please select any Value to perform that operation : ")
        print(Please_select_operation)
        operation_choosen=int(input("Please select any Value to perform that operation : "))
        for x in range(1):
            if operation_choosen==1:
                print(n1+n2)  
            elif operation_choosen==2:
                print(n1-n2)
            elif operation_choosen==3:
                print(n1*n2)
            elif operation_choosen==4:
                print(n1/n2)
            elif operation_choosen==5:
                print(n1%n2)
            elif operation_choosen==6:
                print(n1//n2)
            else : 
                print("Wrong Input, Please ReEnter ", operation())

    else:
        print("Thank You !!")
operation()
#Answer 3:
def octal_conversion():
    import math
    print("Mini Octal Conversion ON ")
    n=(input("Perform Operation Y or N : "))
    if n=='Y' or n=='y':
        n1=int(input("Enter No_To_Convert : "))
        store_ref2=n1
        store_ref=[]
        for x in range(20):
            if math.floor(n1%8)!=0 or (n1==8 or n1==80 or n1==88):
                c=math.floor(n1%8)
                n1=n1/8
                store_ref.append(c)
            else:
                break
        t=store_ref[::-1]
        t12=''
        for x in range(len(t)):
            t12+=str(t[x])
        print("The Octal for '{}' is : {}".format(store_ref2,t12))

    else:
        print("Thank You !!")
octal_conversion()
#Answer 4:
n1=float(input("Enter any Number : "))
print("{:.2f}".format(n1))

#Answer 5:
v1=input("enter any string1 : ")
v2=input("enter any string2 : ")
v3=input("enter any string3 : ")
print(f"{v1} {v2} {v3}")

#Answer 6:
string1=input("Enter any string : ")
print("UpperCase for ur Input is : ",string1.upper())

#Answer 7:
string2=input("Enter any string : ")
count=0
for x in string2:
    count+=1
print("Length of the String is : ",count)

#Answer 8:
string3=input("Enter any string : ")
print("Even Position of a string is : ",string3[::2])

#Answer 9:
radius=int(input("Enter any Radius of a Circle : "))
print("The Area of a Circle is : ",3.141*(radius**2))

#Answer 10:
#Question Not Understandable
    
#Answer 11:
string4=input("Enter any string : ")
reverse=string4[::-1]
if string4==reverse:
    print("Entered string is palindrome ")
else:
    print("Not palindrome")

#Answer 12:
string5=input("Enter any string : ")
for x in string5:
    print(f"Ascii Value for {x} is : {ord(x)} ",)

#Answer 13:
no1=int(input("Enter any number between '0-255' : "))
if no1 in range(256):
    print(f"Character for the no '{no1}' is : {chr(no1)} ",)
else:
    print("Not a Valid Number ")

#Answer 14:
para=input("Enter any ParaGraph : ")
a22=para.split()
print("Total Word Length is : ",len(a22))


#Answer 15:
Enter_ur_Personal=input("Enter_ur_Personal Data : ")
newData=[x for x in Enter_ur_Personal]
# print(newData)
for x in range(len(newData)-1):
    if newData[0]==' ':
        newData.pop(0)
    elif newData[len(newData)-1]==' ':
        newData.pop(len(newData)-1)
else :
    print("ALL DATA IS CORRECT & SAVED IN MY DB")
t1124=''
for x in range(len(newData)):
    t1124+=str(newData[x])
print(t1124)


#Answer 16:
no143=input("Enter any number : ")
print("Reversed of entered no is : ",no143[::-1])

#Answer 17:
v1143=input("enter any string1 : ")
v2143=input("enter any string2 : ")
new143=[]
cnt=0
cnt2=0
t1=''
if len(v1143)==len(v2143):
    for x in range(len(v1143)+len(v2143)):
        if x%2==0:
            new143.append(v1143[cnt])
            cnt+=1
        else:
            new143.append(v2143[cnt2])
            cnt2+=1
    for x in range(len(new143)):
            t1+=str(new143[x])
    print("Final OutPut for Alternating string : ",t1)
else:
    print("Please enter same length for both string")

#Answer 18:
vowels=['A','E','I','O','U']
str122=input('Enter any String : ')
upp122=str122.upper()
c122=0
for x in upp122:
    if x in vowels:
        c122+=1
print("Total Vowels In Ur Sting is : ",c122)

#Answer 19:
taken=input("Enter Data to remove all Special char & Digits : ")
output=''
for x in taken:
    if x.isalpha():
        output+=x
print("After Removing all Special & Digits from the Input is : ",output)

#Answer 20:
Frnd1=input("What u Know Abt ur Frnd2 : ").lower()
Frnd2=input("What u Know Abt ur Frnd1 : ").lower()
if Frnd1==Frnd2:
    print("Data Matched")
else:
    print("U Know Ntg")

#Answer 21:
import sys
data=input("DATA NEEDED : ")
print("Size of ur DATA is : ",sys.getsizeof(data))
print("Length of DATA is : ",len(data))


# Answer for reverse a string by its word
tsunami=input("Enter any Short Para : ")
a1233=tsunami.split()
a1233.reverse()
print("Reverse for a para is ",a1233)
