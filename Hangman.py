# Input word
# Process word
# Divide letter by letter
# funkcja def z trafianiem w literke

word_input = input("Enter a word: ")
word_len = len(word_input)
print(word_len)
iteration_letter = 0
list_letter = []
while word_len != iteration_letter:
    a = word_input[iteration_letter]
    list_letter.append(a)
    iteration_letter += 1

def Miranda():
    print("Welcome in hangman")
    letter_check = input("Choose a letter")
    if letter_check in list_letter:
        print("Trafiłes")

Miranda()


print(list_letter)




