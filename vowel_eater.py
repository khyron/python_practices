user_word = input("enter a word:")    # Prompt the user to enter a word
user_word = user_word.upper()
consonants=""
# and assign it to the user_word variable.

for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        consonants += letter + "\n"
    
print(consonants)
    