# PIG LATIN
# if word starts with a vovel, add 'ay' to end
# if starts with nouns 'a,e,i,u", put first letter at the ednd, and add 'ay

def pig_latin(word):
    first_letter = word[0]
    # check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        #word fron index 1 to end
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word
print( pig_latin('word') )
print( pig_latin('apple') )
