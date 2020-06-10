x = [1,2,3,4]
y = [1,2,3,4]

def compare_lists(x, y):
    count = 0

    if len(x) != len(y):
        print ("The lists are not the same")
        exit
    elif len(x) == len(y):
        for i, j in zip(x, y):
            if i != j:
                print ("The lists are not the same")
                exit
            else:
                count += 1
        if count == len(x):
            print ("The lists are the same")
print(compare_lists(x, y))