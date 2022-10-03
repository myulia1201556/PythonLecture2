# 5. Реализуйте алгоритм перемешивания списка.

list = ["Программист", 2022, 3,14, "True"]
# print(list)
# import random
# random.shuffle(list)
# print(list)

# using Fisher–Yates shuffle Algorithm
 
import random
print ("The original list is : " + str(list))
 
for i in range(len(list)-1, 0, -1):     
    j = random.randint(0, i + 1)   # Pick a random index from 0 to i      
    list[i], list[j] = list[j], list[i]
    
print ("The shuffled list is : " +  str(list))