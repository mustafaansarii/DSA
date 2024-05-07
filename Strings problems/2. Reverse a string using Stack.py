# https://www.geeksforgeeks.org/problems/reverse-a-string-using-stack/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article

from collections import deque
class Stack:
    def __init__(self):
        self.stack=deque()

    def insert(self,x):
        self.stack.append(x)

    def remove(self):
        if len(self.stack) is not None:
            self.stack.pop()
    def _print(self):
        if len(self.stack) is not None:
            for i in self.stack:
                print(i,end=' ')

    def reverse(self):
        rstack=Stack()
        while self.stack:
            rstack.insert(self.stack.pop())
        self.stack = rstack.stack

if __name__ == '__main__':
    s=Stack()
    s.insert("k")
    s.insert("a")
    s.insert("l")
    s.insert("a")
    s.insert("m")

    s._print()
    s.reverse()
    print()
    s._print()
