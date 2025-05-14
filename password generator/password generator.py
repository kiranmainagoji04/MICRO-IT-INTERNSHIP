import random
import string

print(''.join(random.choice(string.ascii_letters + string.digits) for i in range(12)))
print(''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(16)))
print("" if True else "Error: At least one character set must be selected.")
characters = ''
if True:
    characters += string.ascii_letters
if False:
    characters += string.digits
if True:
    characters += string.punctuation
if not characters:
    print("Error: At least one character set must be selected.")
else:
    print(''.join(random.choice(characters) for i in range(16)))