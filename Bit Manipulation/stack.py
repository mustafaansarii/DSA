class Stack:
    def __init__(self,size):
        self.stack=[]
        self.size=size
    def add(self,data):
        if self.size>len(self.stack):
            self.stack.append(data)
            return data
        if self.size==len(self.stack):
            return "Overflow stack"
    def display(self):
        return self.stack

stack=Stack(1)
stack.add(12)
stack.add(2)
stack.add(32)
stack.add(12)
print(stack.display())

