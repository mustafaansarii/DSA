# https://www.geeksforgeeks.org/problems/palindrome-string0817/1
from collections import deque
from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def insert(self, x):
        self.stack.append(x)

    def _print(self):
        return list(self.stack)

    def reverse(self):
        rstack = Stack()
        while self.stack:
            rstack.insert(self.stack.pop())
        return rstack

    def check_palindrome(self):
        return list(self.stack) == list(self.reverse().stack)

if __name__ == '__main__':
    s=Stack()
    s.insert("m")
    s.insert("a")
    s.insert("m")
    # s.insert("u")
    # s.insert("m")
    print(s._print())

    s.reverse()
    print(s.check_palindrome())


