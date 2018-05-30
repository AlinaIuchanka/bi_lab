def generate_numbers(number=20):
    square_dict = {}
    # Call int() for correct working from runner
    for i in range(1, int(number) + 1):
        square_dict[i] = i**2
    return square_dict


def count_characters(count_me_string=""):
    letter_dict = {}
    for letter in count_me_string:
        letter_dict[letter] = count_me_string.count(letter)
    return letter_dict


def __fizzbuzz_convert(number):
    loop_out = ""
    if number % 3 == 0:
        loop_out += "Fizz"
    if number % 5 == 0:
        loop_out += "Buzz"
    if loop_out == "":
        loop_out += str(number)
    return loop_out


def fizzbuzz():
    fizzbuzz_list = []
    for number in range(1, 101):
        fizzbuzz_list.append(__fizzbuzz_convert(number))
    return fizzbuzz_list


def __is_happy(number):
    res = number
    res_list = []
    while res != 1 and res not in res_list[: -1]:
        number_str = str(res)
        res = 0
        for i in number_str:
            res += int(i) ** 2
        if res not in res_list:
            res_list.append(res)
    return res == 1


def happy_numbers(number=100):
    happy_list = []
    # Call int() for correct working from runner
    for num in range(1, int(number) + 1):
        if __is_happy(num):
            happy_list.append(num)
    return happy_list


def is_palindrome(palindrome_string=""):
    palindrome_string = (''.join(symbol
                                 for symbol in palindrome_string.casefold()
                                 if symbol.isalnum()))
    return palindrome_string == palindrome_string[::-1]
