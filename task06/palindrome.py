def is_palindrome(palindrome_string=""):
    palindrome_string = (''.join(symbol
                                 for symbol in palindrome_string.casefold()
                                 if symbol.isalnum()))
    return palindrome_string == palindrome_string[::-1]
