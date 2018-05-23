# https://py.checkio.org/en/mission/right-to-left/
import re

input_string = input("Input strings separated by ,\n")
input_list = (list(
    filter(None, re.split(",", input_string.replace("right", "left")))))
print(','.join(input_list))
