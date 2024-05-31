# https://www.geeksforgeeks.org/problems/get-minimum-element-from-stack/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article
class stack:
    def __init__(self):
        self.s = []
        self.temp = []
        self.minEle = None

    def push(self, x):
        if len(self.temp) == 0 or x <= self.temp[-1]:
            self.temp.append(x)
        self.s.append(x)

    def pop(self):
        if not self.s:
            return -1
        if self.s[-1] == self.temp[-1]:
            self.temp.pop(-1)
        return self.s.pop(-1)

    def getMin(self):
        if not self.temp:
            return -1
        return self.temp[-1]

if __name__ == '__main__':
    stack().push(23)
    stack().push(34)
    stack().push(3)



