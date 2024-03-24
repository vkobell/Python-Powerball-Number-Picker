#Project Name: Powerball Number Picker
#Author: Valerie Kobell
#Constraints: Generate five random numbers between 1 and 69 and generate one number between 1 and 26
#Make sure it won't pick the same number twice
import random
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
list3 = []

for i in range(6): #replace this with while loop; will iterate until list3 has length of 6
    if i<5:
        if i == 0:
            num = random.choice(list1)
            list3.append(num)
        else:
            num = random.choice(list1)
            if num not in list3:
                    list3.append(num)       
    else:
        num = random.choice(list2)
        if num not in list3:
                list3.append(num) 
                
#list1_str = ", ".join(str(element) for element in list1)
#list_1_five = list1[0:5]
#print (list1_str)

list_1st_five = list3[0:5]
list_str = ", ".join(str(element) for element in list_1st_five)
#print (list_str)

print(f"\tNumber Picks: {list_str}\n\tPowerball Number: {list3[5]}\n\tType exit to close.") #if list3 has a length of 6

#for value in list3:
    #print(value, end=" ")
    
#list1_str = ", ".join(str(value) for value in list1)
