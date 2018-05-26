# Use a list comprehension to construct
# the list ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
list1 = ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']
print(list1)

# Use a slice on the above list to construct
# the list ['ab', 'ad', 'bc'].
list2 = list1[:: 2]
print(list2)

# Use a list comprehension to construct
# the list ['1a', '2a', '3a', '4a'].
list3 = ['1a', '2a', '3a', '4a']
print(list3)

# Simultaneously remove the element '2a'
# from the above list and print it.
list3.remove('2a')
print(list3)

# Copy the above list and add '2a' back into the list
# such that the original is still missing it.
list4 = list(list3)
print("Old list = {old_list}; New list = {new_list}".
      format(old_list=list3, new_list=list4))

list4.append('2a')
print("After append: Old list = {old_list}; New list = {new_list}".
      format(old_list=list3, new_list=list4))
