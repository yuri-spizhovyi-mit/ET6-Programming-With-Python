from collections import deque

def is_palindrome(word):
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
