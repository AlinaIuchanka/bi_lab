

# Define a function generate_numbers(number) which returns a dictionary
# where the keys are numbers between 1 and n (both included)
# and the values are square of keys. n – function argument. Default is 20.
def generate_numbers(number=20):
    square_dict = {}
    for i in range(1, number + 1):
        square_dict[i] = i**2
    return square_dict


# Define a function count_characters(count_me_string)
# which count and return the numbers of each character
# in a count_me_string argument.
def count_characters(count_me_string=""):
    letter_dict = {}
    for letter in count_me_string:
        letter_dict[letter] = count_me_string.count(letter)
    return letter_dict


print(generate_numbers(3))
print(generate_numbers())
print(count_characters("abcdefgabc"))
