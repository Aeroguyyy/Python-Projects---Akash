import math
import matplotlib.pyplot as plt 
import numpy as np 


			#DATA TYPES #
"""
my_list = [1,2,3,'edureka','pyplot', 3.24,122]
my_list2 = [3,5,6,'Visa', 'Avinisha','Piggi']
print(my_list[:]) #Accesing all the element
print(my_list[3]) #accesing the thirdd element of the list
print(my_list[0:4])
print(my_list[3][2])
print(my_list[0:5:2]) #Accesing from index 0 to 4 and jumping two elemnts insteaad of 1

my_list.append ([555,12])
print(my_list)
my_list2.extend([555,12])
print(my_list2)

my_list.insert(1,'insert_example')
print(my_list)

print(my_list + ['Just for example']) #Concatenation
print(my_list * 2) #Multiply
print(my_list)
 """


"""

new = [5 , 6 , 7 , 19 ]
print(len(new))
print(sorted(new))
new.sort(reverse=True)
print(new)
new.reverse()
print(new)
"""


"""
#Intilaize elements in the dictionary

my_dict  = {1: 'Python' , 2: 'Java'}
my_dict2 = dict({1: 'C++', 2: 'Ruby'})
print(my_dict)
print(my_dict2)


#Accesing the elements of the dictionary
my_dict = {'First':'Python', 'Second': 'Java'}
print(my_dict['First']) #Get value by keys
print(my_dict.get('Second'))

#Adding and changing elents in the dictionary
my_dict = {'First':'Python', 'Second': 'Java'}
print(my_dict)
my_dict['Second'] = 'c++' #change the value of the key second
print(my_dict)
my_dict['Third'] = 'Ruby' #add new key, value pair
print(my_dict)

#Other Functions
my_dict = {'First':'Python', 'Second': 'Java', 'Third':'C++'}
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())


#String data types

my_str = 'Welcome to the Tutorial'
print(len(my_str))
print(my_str.lower())
print(my_str.upper())
print(my_str.partition('')) #break string into tuple
#Convert string to tuple
print(my.str.split('')) #strings to array
print(my_str.replace('Welcome','Hello, welcome'))


"""
#Assignment operator

"""
a = 5
add, sub, mul,div,rem,expo = 0,0,0,1,1,1

add += a #Add value a with add and assign to add
#add = add + a 
print(add)

sub -= a 
print(add)

mul *= a 
print(a) 

expo **=a 
print(expo)
"""
#Comaprison operator

"""
a =5
b = 6

print(a==b)
print(a != b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)

"""
#Logical opertor
#and = True if both are true
# or = True if either is true
# not = gives the opposite 

"""
"""
#Simple if else statements
'''
a = 10
b = 23

if a==b:
	print("THey are equal")
elif a> b :
	print ("A is greater")
else :
	print(" b is larger")


# nested if else statements

n = int(input("Enter a number:"))
if n >= 0:
	if n == 0:
		print("Enter number is zero")
	else: 
		print("Entered a postive no")
else:
	print("ENtered a negative no")


'''
'''
for i in range(1, 20 , 2):
	for j in range(20,30,2):
		print(i)
	print(j)
print('\n')
'''
#while loops
"""
second = 10
while second >= 0:
	print(second, end= '->')
	second -=1
	print('\n')
print('Blastoff!')

"""
'''
counter = 0
while counter < 3:
	print("Hello")
	counter = counter + 1
else:
	print("Why your not replying bro?")

'''
#Functions
def add(x,y): #you define a function using def keyword
	print('The sum of a and b is:', (x + y))

def multiply(x,y):
	print('The product of x and y is:', (x*y))

add(5,10)
multiply(7,5)
add(7,13)
multiply(5,20)



















