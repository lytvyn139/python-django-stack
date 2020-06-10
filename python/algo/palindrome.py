def isPalindrome(s): 
    rev = ''.join(reversed(s)) 
    if (s == rev): 
        return True
    return False

s = "racecar"
ans = isPalindrome(s) 
if (ans): 
    print("Yes") 
else: 
    print("No") 

#################################################

def string(int):
    ns=""
    for i in range(len(int)-1,-1,-1):
        ns+=(int[i])
        print(ns)
    if ns==(int):
        return True
    else:
        return False

x = string("racecar")
print(x)
    

def isPal(stringInput):
    for i in range(0, len(stringInput)//2, 1):
        if stringInput[i] != stringInput[len(stringInput)-1-i]:
            return False
    return True

print(isPal("pottopdlfjds"))
print(isPal("racecar"))