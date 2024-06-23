# below function takes input of list and returns list with elements multiplication of two :

def multiply_by_two(inputlist: list):
    mylist = []

    for x in inputlist:
        y = x * 2
        mylist.append(y)
    return mylist

# Calling function
l1 = [1, 2, 6, 7]
print("Output of list is :", multiply_by_two(l1))




