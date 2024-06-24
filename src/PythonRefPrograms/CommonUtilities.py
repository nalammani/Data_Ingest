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


# EVEN NUMBERS :

def even_numbers():
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for x in list:
        if 2 != 0:
            continue
    # print(x)
    return list


even_numbers()


# Remove duplicates :
def remove_duplicate(input: list):
    unique_list = []
    for item in input:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


list = [0, 0, 1, 1, 2, 2, 3, 4, 4, 5, 5, 6, 6, 7]
print(remove_duplicate(list))


# Removw zero's:
# the below program is not working as it modifying and iterating the list:

def remove_zero(input: list):
    print("remove_zero executing:")
    print(input)
    for x in input:
        print(x)
        if x == 0:
            input.remove(x)
            print(input)
    return input


list = [0, 0, 1, 2, 3, 0, 4, 5]
print(remove_zero(list))


# However, Python's for loop is not designed to handle modifications to the list it is iterating over. This can lead to skipping elements or unintended behavior.


# Remove zero's :
def remove_zeros(input: list):
    my_list = []
    for x in input:
        if x != 0:
            my_list.append(x)
    return my_list


list = [0, 0, 1, 2, 3, 4, 0, 5]
print(remove_zeros(list))


# zero's at starting of the list :

def starting_zeros(zero : list):
    nonzero_list = []
    zero_list = []
    for x in zero:
        print(x)
        if x == 0:
            zero_list.append(x)
        else:
            print(x)
            nonzero_list.append(x)
    return zero_list + nonzero_list


list = [1, 3, 0, 5, 0, 6, 0]
print(starting_zeros(list))

# maintain the elements having difference of two :
def difference_of_two(input : list):
