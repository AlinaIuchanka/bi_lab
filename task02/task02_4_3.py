# https://py.checkio.org/en/mission/index-power/
import re

input_string = input("Input an array:\n")
input_number = int(input("Input a number:\n"))
input_array = list(map(int, filter(None, re.split("\D+", input_string))))
out = -1
if input_number < len(input_array):
    out = input_array[input_number] ** input_number
print(out)
