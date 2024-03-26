print("Hello and welcome to my little stupid game.")

while True:
    
    vir = input("Give me a word: ") 
    var = vir.upper()
    
     #bei leerzeichen zusammenschreiben lassen oder so
     
    print("You choose %s" %var)

    blanks = list("_" * len(var))
    
    death = 0

    while "_" in blanks:
        
     litter = input("Gimme a letter, that is part of the word: ")
     letter = litter.upper()


     if letter in var:
         
            for i, j in enumerate(var):
               if j == letter:
                blanks[i] = j
             
            print("true")
            print(" ".join(blanks))
    
     else:
         
            print("false")
            print(" ".join(blanks))
            death = death+1
            print("schon %d mal versagt" %death)
     
    print("You guessed the word, well played! Ready for another round?")