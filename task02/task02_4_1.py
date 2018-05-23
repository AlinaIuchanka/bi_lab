# https://py.checkio.org/en/mission/even-last/
# Sums even-indexes elements and multiply at the last
import re


def even_last(array):
    out = sum(array[:: 2])
    if array:
        out *= array[-1]
    return out


input_string = input("Input an array:\n")
input_array = list(map(int, filter(None, re.split("\D+", input_string))))
print(even_last(input_array))
