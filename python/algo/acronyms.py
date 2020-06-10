my_string = 'national Baseball whatever'
def acronyms(param):
    result = ''
    splited_string = param.split(' ')
    for element in splited_string:
        result += element[0].upper()
    return result
print(acronyms(my_string))

stringinput = 'national Baseball whatever'
def acronymizer(stringinput):
    acronym = ''
    for i in range(0, len(stringinput), 1):
        if stringinput[i] == ' ':
            acronym += stringinput[i+1]
    return acronym.upper()

print(acronymizer(stringinput))


def acronym(phrases):
    acronym = ""
    for word in phrases.split():
        acronym = acronym + word[0].upper()
    return acronym


print (acronym("national basketball association"))