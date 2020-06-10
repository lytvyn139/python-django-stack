input_string = "())(" #FALSE
def is_parentheses_valid(input_string):
    count = 0;
    for i in range(0, len(input_string), 1):
        if input_string[i] == "(":
            count +=1
        elif input_string[i] == ")":
            count -=1
        if count < 0:
            return False
    if count != 0:
        return False
    else: 
        return True

print(is_parentheses_valid(input_string))


open_list = ["[","{","("] 
close_list = ["]","}",")"] 
# Function to check parentheses 
def check(myStr): 
    stack = [] 
    for i in myStr: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return "Unbalanced"
    if len(stack) == 0: 
        return "Balanced"
    else: 
        return "Unbalanced"
# Driver code 
string = "{[]{()}}"
print(string,"-", check(string)) 
string = "[{}{})(]"
print(string,"-", check(string)) 
string = "((()"
print(string,"-",check(string)) 