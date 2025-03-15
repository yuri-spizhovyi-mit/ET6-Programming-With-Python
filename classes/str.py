import string

#
print(string.ascii_uppercase)
print(string.ascii_lowercase)
print(string.digits)
print(string.punctuation)


def build_shift_dict(shift):
    """
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to a
    character shifted down the alphabet by the input shift. The dictionary
    should have 52 keys of all the uppercase letters and all the lowercase
    letters only.

    shift (integer): the amount by which to shift every letter of the
    alphabet. 0 <= shift < 26

    Returns: a dictionary mapping a letter (string) to
             another letter (string).
    """
    pass  # delete this line and replace with your code here


## Input: int of shift  0 <= shift < 26
# lc = 'abcdefghijklmnopqrstuvwxyz'

# uc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


"""Example
shift = 3
output = {'a': 'd', 'A': 'D'}
"""
lc = string.ascii_lowercase
uc = string.ascii_uppercase
output = {}
shift = 5
for letter in lc:
    if lc.index(letter) + shift <= 25:
        output[letter] = lc[lc.index(letter) + shift]
    else:
        output[letter] = lc[lc.index(letter) + shift - 26]
for letter in uc:
    if uc.index(letter) + shift <= 25:
        output[letter] = uc[uc.index(letter) + shift]
    else:
        output[letter] = uc[uc.index(letter) + shift - 26]

message = "Hello, World!"  # 'Mjqqt, Btwqi!'
c_message = ""
for letter in message:
    if letter in output:
        c_message += output[letter]
    else:
        c_message += letter

print(output)
print(c_message)
