# https://py.checkio.org/en/mission/secret-message/
message = input("Input a message:\n")
print(''.join([letter for letter in message if letter.isupper()]))
