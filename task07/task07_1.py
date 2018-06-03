import re


# 1
text = 'kdfei.a45t@epam.by email Hgt_dYg@google.com'

re_email = r"\b[a-zA-Z][.?|\w+]*@[a-zA-Z]+\.[a-zA-Z]+\b"
for match in re.findall(re_email, text):
    print(match)

# 2
print()
text = 'root umbrella for makes'

re_word = r"\b[\w]{3,5}\b"
for match in re.findall(re_word, text):
    print(match)

# 3
print()
text = 'root45 um2brella for 156 makes'

re_word = r"\d+"
for match in re.findall(re_word, text):
    print(match)

# 4
print()
text = '_root umbrella_for makes'
out = ""

for symbol in text:
    if symbol == " ":
        out += "_"
    elif symbol == "_":
        out += " "
    else:
        out += symbol

print(out)
