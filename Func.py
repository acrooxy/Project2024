# def name_of_function():
# Snake casing is all lowercase with underscores bteween words

def simply_function():
    print('Hello')

simply_function()

def name():
    name1 = input('What is your name?\n')
    print('Hello {}'.format(name1))

#name()
def name2(nam):
    print('Hello {}'.format(nam))

name2('Damianek')

def farenheit_celcius(argument):
    a = argument*1.8 + 32
    print(a)
farenheit_celcius(100)

def add_function(num1,num2):
    return num1+num2

print(add_function(1,4))

result = add_function(2,8)
print(result)

def even_check(number):
    result = number % 2 == 0
    return result

print(even_check(22))
even_check(5)

def list_even(num_list):
    for x in num_list:
        if x % 2 == 0:
            print(x)
        else:
            continue
list_even([1,2,3,4,44,443,553534,34343,44])

# Tupple unpacking
stock_prices = [('APPL', 200), ('GOOG', 400), ('MSFT', 100)]

for item in stock_prices:
    print(item)

for ticker, price in stock_prices:
    print(price + (0.1*price))

example = [1,2,3,4,5,6,7]

from random import shuffle
shuffle(example)
print(example)

def shuffle_list(arg):
    a = []
    for i in arg:
        a.append(i)
    shuffle(a)
    print('Your shuffled list is {}'.format(a))
    return a

a = shuffle_list([1,2,3,4,56,65,54])

print(a, 'can be recalled as it saved to the value')

def Shuffle_game():
    from random import shuffle, randint
    a=1
    choice = 'X'

    possibilities = []
    print(possibilities)
    while len(possibilities) < 3:
        #possibilities.append(randint(1,3))
        possibilities.append(a)
        a += 1
    print(possibilities)
    shuffle(possibilities)
    print('Ball is in', possibilities[0])


    choice = int(input("Which cup do you want to choose? \n"))
    print('Choice', choice)
    print(type(possibilities[0]), type(choice))
    if choice == possibilities[0]:
        print('You win!')
    else:
        print('You Lose! - Possibilities - {}, choice - {}'.format(possibilities, choice))

#Shuffle_game()

# *args and **kwargs

def myfunc(*args): #treat *args as tuple of arguments, no miniumum and maximum, dynamically adding paramiters
    print(sum(args) * 0.05) # after star I can call it however I want, doesnt have to be args
    print(args)
    return sum(args) * 0.05

myfunc(40,60)

def myfuncc(**kwargs): # kwargs for dictionary
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

myfuncc(fruit='apple', veggi = 'lettuce')

def myfuncakw(*args, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['food']))
    print(' args ', args, ' kwargs ', kwargs)
myfuncakw(10,20,30, fruit='orange', food = 'eggs', animal = 'doog')


def myfunc(*args):
    list_a = []
    for a in args:
        if a % 2 == 0:
            list_a.append(a)
        else:
            continue
    return list_a


def myfunc(a_string):
    word_index = 0     # zmienna indexu slowa
    new_word = ''      # zmienione slowo
    #print('Len = ', len(a_string))  # sprawdzenie
    while len(a_string) > word_index: # dopoki dlugosc slowa dluzsza od indexu obliczanego


        if (word_index+1) %2 != 0:          # jesli nie even
            #print(a_string[word_index]) # jaki index robimy
            new_word = new_word + a_string[word_index].lower()


        elif (word_index+1) % 2 == 0:
            new_word = new_word + a_string[word_index].capitalize()


        word_index +=1
    #print(a_string, word_index, new_word)
    print('New word: ', new_word)
myfunc('Hipopotam')


def lesser_of_two_evens(a, b):
    # the lesser of two given numbers if they are even
    if a and b % 2 == 0:
        if a < b:
            print(a)
            return a
        elif b < a:
            print(b)
            return b
    # but returns greater if one or both odd

    elif a and b % 2 != 0:
        if a > b:
            print(a)
            return a

        elif b > a:
            print(b)
            return b

lesser_of_two_evens(4,7)

##### Write a function takes a two-word string and returns True if both words begin with same letter
def funn(word1, word2):
    if word1[0] == word2[0]:
        print("True")
        return True
    else:
        print('not same')


funn('ja', 'hjem')

# MASTER YODA: Given a sentence, return a sentence with the words reversed

def reverse_sentence(sentence):
    new_sentence = ''
    #new_sentence.join(text.split()[::-1])
    temp_sentence = sentence.split()
    print(temp_sentence)
    temp_sentence.reverse()
    print(temp_sentence)


reverse_sentence('Sentence that does not have to make any sense')

