a = 5
b = 2*a
print(b)
print(a)

print(len('I am Damian'))
mystring = 'Hello World'
print(mystring[6:])
print(mystring[::3])
print(mystring[::-1])
print(mystring.find('l'))
name = 'sam This is a string'
# name[0] = 'P' Not correct
last_letters = name[1:]
print(last_letters)
last_letters='P' + last_letters
print(last_letters)
print(last_letters.split('i'))
 # dot format method
print('This is a string {}'.format('Inserted'))
print("The {2} {1} {0}".format('fox', 'brown','quick'))
print("The {q} {b} {f}".format(f='fox', b='brown',q='quick')) # keywords method

# Float formatting follows "{value:width.precision f}"
result = 100/777
print(result)
print('The result was {r:10.5f}'.format(r=result)) # {value:space for the number.how many numbers}
name = "Jose"
age = 3
print(f"Hi, his name is {name} and he is {age}.")

# LISTS
a_list = ['STRING', 100, 12.5]
print(len(a_list))
print(a_list[1])
li = [0, 1, 2.3]
print(a_list + li) # to save changes I need to assign it to new value
new_list = a_list + li

new_list[0] = 'ONE ALL CAPS'
print(new_list)
new_list.append('New item six')
print(new_list)
print(new_list.pop())
alphabet = ['a', 'b', 'c', 'x', 'o', 'q']
print(alphabet.sort())
sorted_alphabet = alphabet # to run sorted list we need to assign it to new value
print(sorted_alphabet)
sorted_alphabet.reverse()
print(sorted_alphabet)

DictA = {'key1':'value1', 'key2':'value2'}
print(DictA['key1'])
prices_lookup = {'apple':2.99, 'oranges':1.99, 'milk':5}
print(prices_lookup['milk'])
d = {'k1':123, 'k2':[0,1,2,3.4],'k3':{'insideKey':100}}

print(d['k3']['insideKey'])

d = {'key1':['a','b','c']}
mylist = d['key1']
letter = mylist[2]
print(letter)
print(letter.upper())
print(letter)

better_method = d['key1'][1] #Adding new value to Dict
print(better_method)
d['k3added'] = 300
print(d)

#assigning new value to existing key

d['key1'] = 'NEW VALUE'
print(d)

print(d.keys())
print(d.values())

print(d.items()) #Tuples

T = (1,2,3)
mylistX = [1,2,3]
print(type(T), type(mylistX))
print(T[0])

tt = ('a','a','b','c','a')
print(tt.count('a'))
print(tt.index('b'))

myset = set()
print(myset)
myset.add(1)
print(myset)
myset.add(2)
myset.add(3)
myset.add(3) #only one unique value
print(myset)
mylisttt = [1,1,1,1,1,2,2,2,2,2,3,443,4,34,34,3,42,43,1,23,123,]
print(set(mylisttt))

print(set('Mississippi'))

#BOOLEANS
ss = True
sss = False
ssss = None
print(ss,sss,ssss)
c = 1 > 2
print(c)
print(1==1)

'h' == 'h' and 2 == 2 #both condition True
True

1 < 2 > 1
1 == 1 or 2 == 1 # at least one condition True

not 400 > 5000 # True - asking for opposit boolean


# if elif else statements (Colons and Indentations (Wciecia))
sum = 0
my_iterable = [1,2,3,4,5,6,7,8,9,10]
for item in my_iterable:
    sum += item
    if item % 2 == 0: # Check for even number
        print(f'Odd Number: {item}')
    else:
        print(item)
    print(sum)

# Proper iteration if we dont need variable
a = 'ekstra'
for _ in a:
    print(_)

my_list2 = [(1,2,3), (5,6,7), (8,9,10)]
for item_a, item_b, item_c in my_list2: # unpacking variables
    print(item_b)

# ittering througt dictionaries
d = {'k1':1, 'k2':2, 'k3':3}

for key, value in d.items():
    print(value)

# Loopes
# while some_boolean_condition:
    # do something
# else:
    # Do something else

x = 0
while x < 5:
    print(f'The current value of x is {x}')
    x += 1
    # pass comment when need to avoid syntax error
    #if the leeter == 'a':
        #continue # and go back to the loop
        #break stops (breaks out) whole loop

for num in range(0,10,3):
    print(num)

print(list(range(0,11,2)))

index_count = 0

for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1

ind_count = 0
word = 'elephant'
for letter in word:
    print('Letter {} is at index {} '.format(letter, ind_count))
    ind_count += 1

# Python ENUMERATE option

word = 'Karynka Konop'
for let in enumerate(word): # creating tuple and enumerating
    print(let)

# option 2
word = 'Damianek'
for ind, lett in enumerate(word): # creating tuple and enumerating
    print('index: ', ind, 'letter: ', lett)

# Zip Function
# Zip function packing two seperate list into the one tuple
# Can be done with more than 2 lists
# Bare it in mind zip function will be able to zip only maximum same numbers at the lists. So if the lists are
# [3,2,1], [1,2,4,6,7], [2,5,6,7,9,0,4,5] The maximum tuples output will be 3 elements in the lists
my_listX1 = [1,2,3]
my_listX2 = ['a','b','c']
zip(my_listX1, my_listX2)
print(zip(my_listX1, my_listX2)) # zip object saved and waiting for you at 0x7f468e56b040> memory block

for itemX in zip(my_listX1, my_listX2):
    print(itemX)

print(list(zip(my_listX1, my_listX2))) #cast it into the list


 # Dicts again

'mykey' in {'mykey':345}
# True

d = {'mykey':345}
print(345 in d.values())

print('mykey' in d.keys())

# min function
mylistY = [10,20,30,40,50,100]
print(max(mylistY)) #MAX
print(min(mylistY)) #MIN

# Importing function from library

from random import shuffle # this function dont returning anything so yuo cant stick it to variable

shuffle(mylistY)
print(mylistY)

from random import randint # choose random INT

aY = randint(0,100)
print(aY)

# Input always accept everything as a string so I need to force it int(input) =

# List Comprehension
AWord = 'DamianNoCoTy'
print(AWord)
mylistA = [x for x in AWord] #appending letter by letter in a list ##ELEMENT FOR ELELENT IN A VARIABLE
print(mylistA)

mylistB = [num for num in range(0,16,3)]
print(mylistB)

mylistC = [num**2 for num in range(0,16,3)]
print(mylistC)

mylistD = [num**2 for num in range(0,16,3) if num%2 == 0] #MODULO # check if the num is even - parzyste
print(mylistD)

Celc = [36.6, 30, 39.2] # Calculator Celcius to Farenheit
mylistE = [num*(9/5) + 32 for num in Celc]


print('Farenheit = ', mylistE)

farenheitA =  []#[32.0, 50.0, 68.0, 94.1]

for temp in Celc:
    farenheitA.append(( (9/5) * temp + 32))

print(farenheitA)

results = [x if x%2==0 else 'ODD' for x in range(0, 11)] # IF ELSE in comprehension, but not advicible
print(results)

# Nestet lists
myListF = []

for x in [2,4,6]:
    for y in [100,200,300]:
        myListF.append((x*y))
print(myListF)

# Comprahension now

myListG = [x*y for x in [2,4,6] for y in [1,10,1000]]

print(myListG)

st = 'Print only the words that start with s in this sentence'
stDone = st.split()
# print(stDone)

for word in stDone:
    if word[0] == 's':
        print(word)
    else:
        continue


a = []
for num in range(0,11):
    a.append(num)
print(a)

stWord = st.split()
tempnum = 0

stWord = st.split()
for word in stWord:
    if len(word) %2==0:
        print('word \'{}\' with letter number {} is Even'.format(word, len(word)))
    else:
        continue


numbers = []
for num in range(0,101):
    numbers.append(num)
print(numbers)

for x in numbers:
    if x%3==0:
        print('Fizz {}'.format(x))
    elif x%5==0:
        print('Buzz {}'.format(x))
    elif x%3==0 and x%5==0:
        print('FizzBuzz {}'.format(x))
    else:
        print(x)


## METHODS AND FUNCTIONS

# .pop , .append
list = [1,2,4,5]
print(list)

help(list.insert)

