#Sets
# 1. Write a program to create an empty set.
# 2. Create a set from a list of elements.
# 3. Write a program, to create new which will contain common elements in two
# different sets.
# 4. Write a program to get unique items from two sets.
# 5. Update the first set with items that don’t exist in the second set.
# 6. Write a program to return a set of elements present in set a or b, but not both.
# 7. Write a program to check if two sets have any elements in common. If yes,
# display the common elements.
# 8. Write a program to remove items from set1 that are not common to both set1
# and set2.
# 9. Write a program to create set of even numbers only.
# 10. Write a program to get size of set.
# 11. Write a program to convert set into tuple and tuple into set.

#Answer 1:
empty_Set=set()

#Answer 2:
list_of_u=[42,28,42]
set_creation=set(list_of_u)
print(set_creation)

#Answer 3:
set4354={66,67,68,69,70}
set2435={66,68,70,72,74}
set3435=set4354.intersection(set2435)
print(set3435)

#Answer 4:

set43541={66,67,68,69,70}
set24351={66,68,70,72,74}
set34351=set43541.union(set24351)
print(set34351)

#Answer 5:
set43542={66,67,68,69,70}
set24352={66,68,70,72,74}
set43542.update(set24352)
print(set43542)

#Answer 6:

#Answer 7:

set435412={66,67,68,69,70}
set243512={66,68,70,72,74}
set343512=set435412.union(set243512)
print("The Common Elements are : ",set343512)

#Answer 8:
set435412={66,67,68,69,70}
set243512={66,68,70,72,74}
temp12=set435412.intersection(set243512)
for x in temp12:
    set435412.remove(x) 
print("The Common Elements are removed: ",set435412)

#Answer 9:
even_Set=set()
for x in range(10):
    if x%2==0:
        even_Set.add(x)
print("Even Set ",even_Set )

#Answer 10:
set4354w2={66,67,68,69,70}
import sys
print("SizeOfSET : ",sys.getsizeof(set4354w2))

#Answer 11:
set4se23={66,67,68,69,70}
print("Converted set into tuple : ",tuple(set4se23))
tuple2324=(66, 67, 68, 69, 70,213)
print("Converted tuple into set : ",set(tuple2324))
