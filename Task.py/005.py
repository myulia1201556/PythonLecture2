# 5. Реализуйте алгоритм перемешивания списка.

list = ["Программист", 2022, 3,14, "True"]

#1
# print(list)
# import random
# random.shuffle(list)
# print(list)


#2
# using Fisher–Yates shuffle Algorithm
 
# import random
# print ("The original list is : " + str(list))
 
# for i in range(len(list)-1, 0, -1):     
#     j = random.randint(0, i + 1)   # Pick a random index from 0 to i      
#     list[i], list[j] = list[j], list[i]
    
# print ("The shuffled list is : " +  str(list))


#3
import random
 
# Display original array
print("Original List: ", list)
 
# Get length of List
n = len(list)
 
#repeat the following for n number of times
for i in range(n):
    #select an index randomly
    j = random.randint(0, n-1)
    #delete the element at that index.
    element=list.pop(j)
    #now append that deleted element to the list
    list.append(element)
print("Shuffled List: ",list)