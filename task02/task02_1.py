# Write a program that check whether a string is palindrome or Not
palindrome_string = input("Input a string:\n").casefold()
palindrome_string = (''.join(symbol for symbol in palindrome_string
                             if symbol.isalnum()))
if palindrome_string == palindrome_string[::-1]:
    print("String is a palindrome")
else:
    print("String isn't a palindrome")
