sentence = input("Enter an English sentence: ")
word = ""
pirate = ""

space = sentence.find(" ")
       while space != -1:
 word = sentence[0:space]
 sentence = sentence[space+1:]
      if word == "hello":
         pirate = pirate + "ahoy" + " "
    elif word == "friend":
        pirate = pirate + "matey" + " "
        else:
        pirate = pirate + word + " "
            space = sentence.find(" ")

 if sentence != "":
    word = sentence
    sentence = ""
     if word == "hello":
                 pirate = pirate + "ahoy" + " "
        elif word == "friend":
         pirate = pirate + "matey" + " "
              else:
        pirate = pirate + word + " "
 
print("Your sentence translated to pirate is:")
print(pirate)