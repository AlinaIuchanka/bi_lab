# Create the list ['a', 'b', 'c'], then create a tuple from that list.
list1 = ['a', 'b', 'c']
tuple1 = tuple(list1)
print(tuple1)

# Create the tuple ('a', 'b', 'c'), then create a list from that tuple.
tuple2 = ('a', 'b', 'c')
list2 = list(tuple2)
print(list2)

# Make the following instantiations simultaneously:
# a = 'a', b=2, c='gamma'. (That is, in one line of code).
a, b, c = 'a', 2, 'gamma'
print("a = {a}; b = {b}; c = {c}".format(a=a, b=b, c=c))

# Create a tuple containing just a single element
# which in turn contains the three elements 'a', 'b', and 'c'.
# Verify that the length is actually 1 by using the len() function.
tuple3 = tuple([('a', 'b', 'c')])
print(tuple3)
print(len(tuple3))
