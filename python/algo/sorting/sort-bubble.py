#my_list = [1,5,3,2,0,8,2,5]
my_list = [3,2,6,4,2]
print(f"orignal list {my_list}")
def bubble_sort(my_list):
    count = 0
    for j in range(1, len(my_list)-1):
        print("\n", "-"*50, "Iteration", j)
        for i in range(len(my_list)-1-j):
        
            print(f"my_list[{i}] value: {my_list[i]}")
            print(f"comparing: {my_list[i]} vs {my_list[i+1]}")
            if my_list[i] > my_list[i+1]:
                my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
                print(f"swapped {my_list[i]} with {my_list[i+1]}")
                print("new my_list: ", my_list)
            else:
                print(f"no need to swap {my_list[i]} < {my_list[i+1]}")
    print(f"# on evaluations {count}")
    return my_list

print(bubble_sort(my_list))


