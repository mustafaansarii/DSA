class MinHeap:
    def __init__(self) -> None:
        self.heap=[]
    
    def insert(self,value):
        self.heap.append(value)
        self.heapify_up(len(self.heap)-1)
        return value
    
    def heapify_up(self,index):
        parent_index=(index-1)//2
        while index>0 and self.heap[parent_index]>self.heap[index]:
            self.heap[parent_index],self.heap[index]=self.heap[index],self.heap[parent_index]
            index=parent_index
            parent_index=(index-1)//2

    def delete(self):
        if len(self.heap)==0:
            raise ValueError("delete from empty heap!")
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
            smallest=index
            if left_index<=last_index and self.heap[left_index]<self.heap[smallest]:
                smallest=left_index
            if right_index<=last_index and self.heap[right_index]<self.heap[smallest]:
                smallest=right_index
            if index==smallest:
                break
            self.heap[smallest],self.heap[index]=self.heap[index],self.heap[smallest]
            index=smallest

    def heap(self,arr,n):
        if len(arr)==0:
            raise IndentationError("Empty! array")
        self.heapify_up()

    

if __name__=="__main__":
    obj=MinHeap()
    print("Heap before insertion:", obj.heap)
    obj.insert(10)
    obj.insert(20)
    obj.insert(30)
    obj.insert(40)
    print("Heap after insertion:", obj.heap)
    obj.delete()
    print("Heap before insertion:", obj.heap)


