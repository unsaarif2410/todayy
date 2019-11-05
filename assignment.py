#1
print('1')
print('''Twinkle, twinkle, little star,
    How I wonder what you are!
            Up above the world so high,
            Like a diamond in the sky.
Twinkle twinkle little star,
    How I wonder what you are''')

print('----------------------------------')
#2
print('2')
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)
print('----------------------------------')
#3
print('3')
from datetime import datetime
print(datetime.now())
print('----------------------------------')
#4
print('4')
r=int(input('Enter radius of circle'))
area=(3.14)*(r**2)
print('area of circle',area)
print('----------------------------------')
#5
print('5')
First_Name=input('Enter First Name')
Last_Name=input('Enter Last Name')
print(Last_Name[len(Last_Name)::-1],'',First_Name[len(First_Name)::-1])
print('----------------------------------')   
#6
print('6')
num1=int(input('Enter 1st number'))
num2=int(input('Enter 2nd number'))
sum=num1+num2
print('sum',sum)
