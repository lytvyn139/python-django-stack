def reverseString(stringInput):
# some code here 
    newstr = ""
    for i in range(len(stringInput)-1, -1, -1):
      newstr += stringInput[i]
    return newstr
print(reverseString("hello")) 