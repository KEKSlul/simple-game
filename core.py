print("Hello and welcome to my little stupid game.")

var = input("Give me a word: ") 


print("You choose " + var)

L = len(var)

print("_" * L)

test = input("Gimme a letter, that is part of the word: ")

if test in var:
    print("true")
else:
    print("false")