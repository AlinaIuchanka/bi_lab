# Write a program that prints the numbers from 1 to 100,
# but for multiples of three print “Fizz” instead of the number and for multiples of five print “Buzz”.
# For numbers which are multiples of both three and five, print “FizzBuzz”


def convert(number):
    loop_out = ""
    if number % 3 == 0:
        loop_out += "Fizz"
    if number % 5 == 0:
        loop_out += "Buzz"
    if loop_out == "":
        loop_out += str(number)
    return loop_out


print("\n".join([convert(number) for number in range(1, 101)]))
