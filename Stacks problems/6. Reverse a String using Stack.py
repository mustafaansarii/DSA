#https://www.geeksforgeeks.org/problems/reverse-a-string-using-stack/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article

from collections import deque


class Stack:
    def __init__(self, size):
        self.stack = deque()
        self.size = size

    def insert(self, data):
        if self.size == len(self.stack):
            return "Stack is full"
        print(f"element inserted in stack: {data}")
        return self.stack.append(data)

    def _print(self):
        for i in range(len(self.stack)):
            print(self.stack[i], end=' ')

    def Reverse(self):
        reversed_string = ''
        while self.stack:
            word = self.stack.pop()
            reversed_string += word[::-1]
            if self.stack:
                reversed_string += ' '
        print(reversed_string)

if __name__ == '__main__':
    stack = Stack(10)

    stack.insert('G')
    stack.insert('e')
    stack.insert('e')
    stack.insert('k')
    stack.insert('s')

    print(stack._print())

    print(stack.Reverse())
