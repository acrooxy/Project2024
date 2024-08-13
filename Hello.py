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