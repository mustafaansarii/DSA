# https://www.geeksforgeeks.org/implement-two-stacks-in-an-array/
from collections import deque
import math

class Twostack:
    def __init__(self, size) -> None:
        self.arr = deque()
        self.size = size
        self.top1 = -1
        self.top2 = size

    def print(self):
        for i in self.arr:
            print(i, end=' ')

    def s1_push(self, x):
        if self.top1 < self.top2 - 1:
            self.arr.appendleft(x)
            self.top1 = self.top1 + 1
        else:
            print("Stack Overflow by element:", x)

    def s1_pop(self):
        if self.top1 >= 0:
            x = self.arr.popleft()
            self.top1 = self.top1 - 1
            return x
        else:
            print("Stack Underflow")
            exit(1)

    def s2_push(self, x):
        if self.top1 < self.top2 - 1:
            self.arr.append(x)
            self.top2 = self.top2 - 1
        else:
            print("Stack Overflow by element:", x)

    def s2_pop(self):
        if self.top2 < self.size:
            x = self.arr.pop()
            self.top2 = self.top2 + 1
            return x
        else:
            print("Stack Underflow")
            exit(1)

Ts = Twostack(5)

Ts.s1_push(1)
Ts.s1_push(2)
Ts.s1_push(3)

Ts.s2_push(11)
Ts.s2_push(12)
Ts.s2_push(13)

print("Stack 1:")
Ts.print()
print("\nStack 2:")
Ts.print()

print("\nPopping from Stack 1:")
print(Ts.s1_pop())
print(Ts.s1_pop())
print(Ts.s1_pop())

print("\nPopping from Stack 2:")
print(Ts.s2_pop())
print(Ts.s2_pop())
print(Ts.s2_pop())
