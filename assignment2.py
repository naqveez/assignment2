
import random as r
arr = []
for i in range(100):
    arr.append(r.randint(1,1000))
exercise = arr[0]
print(arr)
k = 0
for j in range(0, len(arr) ,1):
    if exercise > arr[j] :
     exercise = arr[j]
     k = j
print("Min :", exercise, "   index : ", k)

for j in range(0, len(arr), 1):
    if exercise < arr[j]:
        exercise = arr[j]
        k = j
print("Max :" , exercise , " index :" , k)

sum = 0
for l in range(0, len(arr), 1):
    sum = sum + arr[l]
avg = sum/len(arr)
print("Mean :" , avg)