
L = [10,[3, 5, 8],[[13, 14], 15, 18], 20]

def print_list(lst):
    for x in lst:
        if type(x) is not list:
            print(x,end = ' ')


        else:
            print_list(x)
            
    

print_list(L)

    
