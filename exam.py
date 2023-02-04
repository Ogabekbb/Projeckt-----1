# ex.2
# a = 'GameOver'
# b = 'Over'
# if a.find(b):
#     print("True")
# else:
#     print("False")

# ex.3

import string

# def pan(text):
#     alf = list(string.ascii_lowercase)
#     for i in alf:
#         if text.lower().find(i) != 0:
#             pass
#             return True
#         else:
#             return False

# print(pan(input('Enter - ')))

import string

def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
    return True

string = 'the quick brown fox jumps over the lazy dog'
if(ispangram(string) == True):
    print("Yes")
else:
    print("No")

# ex.1


