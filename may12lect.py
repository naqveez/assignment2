'''

print(``````if/elif/else with input/and``````)

user_input = float(input("enter your GPA :"))
if user_input == 4.0 and user_input >= 3.7:
    print("your grade is A+")
elif user_input < 3.7 and user_input >= 3.5:
    print("your grade is A")
elif user_input < 3.5 and  user_inpit >= 3.0:
    print("your grade is B")
elif user_input < 3.0  and user_input >= 2.5:
    print("your grade is C")
else:
    print("sorry, you are fail")
'''

#user_name = input("enter your name :")
#print("Hello, My name is "  + user_name)

#employee_data = ["sameen" , 23 , "karachi"]
#print("employee name is " +employee_data[0] + " employee age is  " +str(employee_data[1]) + " employee city is " +employee_data[2])
'''
numberlist = [71,45,55,24,15]
for num in numberlist:
    if (num % 5 == 0):
      print(num)

for num in range(10):
    for i in range(num):
        print (num, end=" ") #print number
    # new line after each row to display pattern correctly
    print("\n")
'''
import random as r

for i in range(3):
    print(r.randrange(100,999,5), end=',')

