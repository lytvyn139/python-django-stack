"""
“ String: In-Order Subsets
Create strSubsets(str). Return an array with every possible in-order character subset of str. 
The resultant array itself need not be in any specific order – it is the subset of letters in each 
string that must be in the same order as they were in the original string. Given "abc", return an array that includes 
["", "c", "b", "bc", "a", "ac", "ab", "abc"] (in any order).”
"""
def ios(stringinput, sub = "", i = 0):
    #some code here
    if len(stringinput) == i:
        return [sub]
    else:
        return ios(stringinput, sub + stringinput[i], i+1) + ios(stringinput, sub, i+1)



print(ios("abc"))
