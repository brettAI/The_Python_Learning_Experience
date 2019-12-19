'''
    A test file with information around handling text.

    Quotes:
        Can use both single (') and double quotes (").
        If the string contains one of these, use the other of escape the string, e.g. 'It\'s a new day'

        Multiline string variables can be created with 3 x (")
            """ multi line string
            that carries over to here
            and here"""


    A String is a series of characters - can use '[]' to access a specific charcters
        print(message[0:5])

        Defines the starting point and number of charcters.
        This is all related to 'slicing'

    Some useful message

        .lower()    - changes all characters to lowercase
        .upper()    - changes all characters to uppercase
        .count(str) - Counts how may times 'str' appears in the string
        .find(str)  - Finds the starting place of a string
'''

# variable named `message`

import datetime
message = 'Hello World'

print(message)          # Prints the variable 'message'
print(len(message))     # Prints the length of the variable 'message'

# Prints the charcater in position [0] (first) of the variable 'message'
print(message[0])

try:        # Tries to print a character outside of the message list.
    print(message[11])
except:
    print("error")


print(message.lower())      # Converts the string to lowercase
print(message.upper())      # Converts the string to uppercase
# Counts the number of times the letter 'l' appears in the string
print(message.count('l'))
# Finds the first instance of the string 'l' in the variable message. Returns -1 if the string cannot be found
print(message.find('l'))

# .replace creates a new string
new_message = message.replace('World', 'Universe')
print(message)
print(new_message)
message = message.replace('World', 'Universe')

greeting = 'Hello'
name = 'Bob'

# String concatenation with '+'
message = greeting + ', ' + name
print(message)

# Can also used a formatted string '{}' with .format
message = '{}, {}. Welcome'.format(greeting, name)
print(message)

# Python 3.6 and above
message = f'{greeting}, {name.upper()}. Welcome'
print(message)

# Prints out each of the methods and attributes on this variable 'a string'
# print(dir(name))

# Prints out help about the string type
# print(help(str))

# print(help(str.lower))


person = {'name': 'Jen', 'age': 23}
sentence = 'My name is ' + person['name'] + \
    ' and I am ' + str(person['age']) + ' years old.'
print(sentence)

sentence = 'My name is {} and i am {} years old.'.format(
    person['name'], person['age'])
print(sentence)

# placeholders can be explicitly numbered.
# Can be useful when a varibale needs to be repeated.
sentence = 'My name is {0} and i am {1} years old.'.format(
    person['name'], person['age'])
print(sentence)

sentence = 'My name is {0[name]} and i am {1[age]} years old.'.format(
    person, person)
print(sentence)

sentence = 'My name is {0[name]} and i am {0[age]} years old.'.format(
    person)
print(sentence)

# Similar if managing a list instead of a dictionary
lst = ['Bob', 54]
sentence = 'My name is {0[0]} and i am {0[1]} years old.'.format(lst)
print(sentence)


# from a class
class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('Jane', 34)

sentence = 'My name is {0.name} and i am {0.age} years old.'.format(p1)
print(sentence)

sentence = 'My name is {name} and i am {age} years old.'.format(
    name='Teddy', age=1)
print(sentence)

person = {'name': 'Alexis', 'age': 10}
sentence = 'My name is {name} and i am {age} years old.'.format(**person)
print(sentence)

for i in range(1, 11):
    # Can add a format to pad character lengths
    sentence = 'The value is {:03}'.format(i)
    print(sentence)

pi = 3.14159265
sentence = 'Pi is equal to {}'.format(pi)
print(sentence)

# .#f controls the number of decimals places.
sentence = 'Pi is equal to {:.2f}'.format(pi)
print(sentence)

sentence = '1 MB is equal to {} bytes'.format(1000 ** 2)
print(sentence)

sentence = '1 MB is equal to {:,} bytes'.format(1000 ** 2)  # Comma separated
print(sentence)

sentence = '1 MB is equal to {:,.2f} bytes'.format(
    1000 ** 2)  # Chaining, Comma separated and decimal places
print(sentence)

my_date = datetime.datetime(2019, 11, 30, 7, 33, 51)
sentence = '{}'.format(my_date)
print(sentence)

sentence = '{:%B %d, %Y}'.format(my_date)
print(sentence)

sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(
    my_date)
print(sentence)


# Escape Characters
# start with a '\' backslash
'''
    \n - new line
    \t - tab
'''
test = 'This is a \n sentence'
print(test)

# Can create a raw string by prefixinf with 'r', the escape charaters are ignored
test = r'This is a \n sentence'
print(test)

test = "Hello world"
rtn = 'Hello' in test   # There is also a 'not in'
print(rtn)


# startswith - also and endswith
print(test.startswith('Hell'))

# split() - returns a List - The reverse is a join()
print(test.split(' '))
split = test.split(' ')
print(split)
joined = ' '.join(split)
print(joined)


# strip removes extract spaces
# can strip from left (lstrip) or right (rstrip)
sent = '      Extra spacing  '
print(sent.strip())
