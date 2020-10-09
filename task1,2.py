arr = [1, 2, 3, 10, 11, 16, 18, 4 ,43, 2, 2, 4]

threshold1 = 2
threshold2 = 4

#assignment: 01 Check if threshold1 and threshold2 exist in arr


twoExistInArray = False
fourExistInArray = False


for element in arr:
    if element == threshold1 and threshold2:
        twoExistInArray = True 
        fourExistInArray = True

print("they exist")
if twoExistInArray and fourExistInArray:
    print("True")
else:
    print("False")
    
    
# assignment: 02 how many times arr contains threshold1 and threshold2?

twoExistInArray = False
fourExistInArray = False
countTwoInArray = 0
countFourInArray = 0

for element in arr:
    if element == threshold1:
       twoExistInArray = True
       countTwoInArray += 1
print("2 esists "+str(countTwoInArray)+" times")

for element in arr:
    if element == threshold2:
       fourExistInArray = True
       countFourInArray += 1
print("4 esists "+str(countFourInArray)+" times")


       
