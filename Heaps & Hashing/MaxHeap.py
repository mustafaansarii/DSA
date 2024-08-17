class Max_Heap:
    def __init__(self) -> None:
        self.heap=[]
    def insert(self,value):
        self.heap.append(value)
        self.heapify_up(len(self.heap)-1)

    def heapify_up(self,index):
        parent_index=(index-1)//2
        while index>0 and self.heap[parent_index]<self.heap[index]:
            self.heap[parent_index],self.heap[index]=self.heap[index],self.heap[parent_index]
            index=parent_index
            parent_index=(index-1)//2

    def delete(self):
        if len(self.heap)==0:
            raise ValueError("delete from Empty Heap!")
        if len(self.heap)==1:
            return self.heap.pop()
        root=self.heap[0]
        self.heap[0]=self.heap.pop()
        self.heapify_down(0)
        return root
    
    def heapify_down(self,index):
        last_index=len(self.heap)-1
        while True:
            left_index=2*index+1
            right_index=2*index+2
            largest=index
            if left_index<=last_index and self.heap[left_index]>self.heap[largest]:
                largest=left_index
            if right_index<=last_index and self.heap[right_index]>self.heap[largest]:
                largest=right_index
            if largest==index:
                break
            self.heap[index],self.heap[largest]=self.heap[largest],self.heap[index]
            index=largest

    

if __name__=="__main__":
    obj=Max_Heap()
    print("Heap before insertion:", obj.heap)
    obj.insert(10)
    obj.insert(20)
    obj.insert(30)
    obj.insert(40)
    print("Heap after insertion:", obj.heap)
    obj.delete()
    print("Heap before insertion:", obj.heap)
