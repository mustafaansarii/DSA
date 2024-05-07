#https://www.geeksforgeeks.org/problems/parenthesis-checker2744/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article
class Stack:
    def is_balanced(self, expression):
        stack = []
        opening_brackets = {'(', '[', '{'}
        closing_brackets = {')': '(', ']': '[', '}': '{'}
        
        for char in expression:
            if char in opening_brackets:
                stack.append(char)
            elif char in closing_brackets:
                if not stack or stack.pop() != closing_brackets[char]:
                    return False
        if stack:
            return False
        else:
            return True

if __name__ == '__main__':
    pc = Stack()
    print(pc.is_balanced("{()}[]"))  
    print(pc.is_balanced("{()[]}"))  
    print(pc.is_balanced("{()[]}("))  
