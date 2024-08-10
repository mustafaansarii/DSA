from collections import deque
class stack:
    def __init__(self):
        self.stack = deque()

    def enqueue(self, x):
        self.stack.append(x)

    def _print(self):
        for i in self.stack:
            print(i, end=' ')

    def dequeue(self):
        self.stack.pop()

    def middle_of_stack(self):
        if len(self.stack) == 0: return "stack is empty!"
        a = (len(self.stack) // 2)
        return self.stack[a]

if __name__ == '__main__':
    my_stack = stack()

    my_stack.enqueue(1)
    my_stack.enqueue(2)
    my_stack.enqueue(3)
    my_stack.enqueue(4)
    my_stack.enqueue(5)

    print("Stack elements:")
    my_stack._print()

    print("\nMiddle of the stack:", my_stack.middle_of_stack())

    my_stack.dequeue()

    print("Stack elements after dequeue:")
    my_stack._print()

    print("\nMiddle of the stack after dequeue:", my_stack.middle_of_stack())

