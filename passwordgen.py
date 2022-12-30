'''
Random Password Generator using Python
Author: Audrey GOUDI
'''

#import the necessary modules!
import random
import string

print('Hello Teacher, Welcome to educ8africa Password generator:')

#input the length of password
length = 12                      

#define data
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

#combine all the data to create an alphabet
alphabet = lowercase + uppercase + numbers + symbols

#use random function to shuffle
temp = random.sample(alphabet,length)

#create the password
password = "".join(temp)

#print the password
print(password)