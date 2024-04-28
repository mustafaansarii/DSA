#https://www.geeksforgeeks.org/problems/parenthesis-checker2744/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article
from collections import deque
class Stack:
    def __init__(self):
        self.stack = deque()

    def Parenthesis_check(self, chars):
        for char in chars:
            if char in ["[", "{", "("]:
                self.stack.append(char)
            else:
                if not self.stack:
                    return False
                current_char = self.stack.pop()
                if current_char == '(':
                    if char != ")":
                        return False
                elif current_char == '{':
                    if char != "}":
                        return False
                elif current_char == '[':
                    if char != "]":
                        return False
        return not self.stack



if __name__ == '__main__':
    PC = Stack()
    print(PC.Parenthesis_check("{()}[]"))
    print(PC.Parenthesis_check("{()[]"))