# 1
def divide_zero():
    try:
        print(5/0)
    except ZeroDivisionError as error:
        print("Error: division by zero")


def print_list_element(thelist, index):
    try:
        print(thelist[index])
    except IndexError:
        print("Error: index not in the list")


def add_to_list_in_dict(thedict, listname, element):
    try:
        l = thedict[listname]
        print("%s already has %d elements." % (listname, len(l)))
    except KeyError:
        thedict[listname] = []
        print("Created %s." % listname)
    finally:
        thedict[listname].append(element)
        print("Added %s to %s." % (element, listname))


# 1
divide_zero()

# 2
print_list_element([1, 2, 3], 5)

# 3
dictionary = {'a': [1, 2, 3]}
print('Old dictionary: ' + str(dictionary))
add_to_list_in_dict(dictionary, 'b', 4)
print('New dictionary: ' + str(dictionary))
