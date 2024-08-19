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

