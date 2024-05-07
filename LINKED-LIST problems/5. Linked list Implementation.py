class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SynglyLL:
    def __init__(self):
        self.head = None

    def len(self):
        if self.head is None: return 0
        count = 0
        n = self.head
        while n:
            n = n.next
            count += 1
        return count

    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return

    def print(self):
        if self.head is None: return "SLL is Empty!"
        n = self.head
        while n:
            print(n.data, end=' ')
            n = n.next

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.insert_begin(data)
            return
        n = self.head
        while n.next:
            n = n.next
        n.next = new_node

    def insert_by_value(self, data, x):
        new_node = Node(data)
        if self.head is None: return "Empty! LL!"
        n = self.head
        while n:
            if n.data == x:
                new_node.next = n.next
                n.next = new_node
                return
            n = n.next
        print(f"{x} Node is not present in LL!")

    def insert_mid(self, data):
        new_node = Node(data)
        if self.head is None:
            self.insert_begin(data)
            return
        mid = self.len() // 2
        n = self.len()
        if n % 2 == 1:
            mid += 1
        n = self.head
        while mid > 1:
            n = n.next
            mid -= 1
        new_node.next = n.next
        n.next = new_node

    def insert_after(self, data, x):
        new_node = Node(data)
        n = self.head
        while n:
            if n.data == x:
                new_node.next = n.next
                n.next = new_node
                return
            n = n.next
        print(f"{x} node is not present in SLL or SLL is Empty!")

    def clear(self):
        self.head = None

    def remove_begin(self):
        if self.head is None:
            raise IndexError("Empty! LL")
            return
        self.head = self.head.next

    def remove_end(self):
        if self.head is None:
            raise IndexError("Empty! LL")
            return
        if self.head.next is None:
            self.head = None
            return
        n = self.head
        while n.next.next:
            n = n.next
        n.next = None

    def delete_Node(self, x):
        if self.head is None:
            raise IndexError("Empty! LL")
            return
        if self.head.data == x:
            self.head = self.head.next
            return
        n = self.head
        while n:
            if n.data == x:
                n.next = n.next.next
            n = n.next
        print(f"{x} node is not present in SLL!")

    def search(self, x):
        if self.head is None:
            raise IndexError("Empty! LL")
            return
        n = self.head
        count = 0
        while n:
            if n.data == x:
                print(f"{x} is present at index {count}")
                return
            count += 1
            n = n.next
        print(f"{x} node is not present in SLL!")

    def search_by_index(self, x):
        if self.head is None:
            raise IndexError("Empty! LL")
            return
        if x > self.len():
            raise IndexError("Given Index is out Of range!")
            return
        if x == 0:
            return self.head.data
        n = self.head
        while x != 0:
            x -= 1
            n = n.next
        print(n.data)

    def delete_by_index(self, x):
        if self.head is None:
            raise IndexError("Empty! LL")
            return
        if x >= self.len():
            raise IndexError("Given Index is out Of range!")
            return
        if x == 0:
            self.head = self.head.next
            return
        if x == self.len() - 1:
            self.remove_end()
            return
        n = self.head
        while x != 1:
            n = n.next
            x -= 1
        n.next = n.next.next

    def Reverse(self):
        if self.head is None:
            raise IndexError ("Empty! LL")
            return
        if self.head.next is None:
            self.head.data
            return
        cur=self.head
        prev=None
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        self.head=prev

if __name__ == "__main__":
    Sll=SynglyLL()

    # Inserting elements at the beginning
    Sll.insert_begin(3)
    Sll.insert_begin(1)
    Sll.insert_begin(7)
    print("Linked List after inserting at the beginning:")
    Sll.print()
    print()
    Sll.Reverse()

    print("\nReversed Linked List:")
    Sll.print()
    # Inserting elements at the end
    Sll.insert_end(9)
    Sll.insert_end(11)
    print("\nLinked List after inserting at the end:")
    Sll.print()
    print()

    # Inserting elements by value
    Sll.insert_by_value(5, 3)  # Insert 5 after node with value 3
    print("\nLinked List after inserting by value:")
    Sll.print()
    print()

    # Inserting element in the middle
    Sll.insert_mid(4)
    print("\nLinked List after inserting in the middle:")
    Sll.print()
    print()

    # Inserting element after a specific value
    Sll.insert_after(8, 5)  # Insert 8 after node with value 5
    print("\nLinked List after inserting after a specific value:")
    Sll.print()
    print()

    # Removing element from the beginning
    Sll.remove_begin()
    print("\nLinked List after removing from the beginning:")
    Sll.print()
    print()

    # Removing element from the end
    Sll.remove_end()
    print("\nLinked List after removing from the end:")
    Sll.print()
    print()

    # Deleting a specific node by value
    Sll.delete_Node(7)
    print("\nLinked List after deleting a specific node by value:")
    Sll.print()
    print()

    # Searching for an element
    Sll.search(9)
    Sll.search(15)  # Searching for a value not in the list
    print()

    # Searching for an element by index
    print("\nElement at index 2:", Sll.search_by_index(2))
    print()

    # Deleting a specific node by index
    Sll.delete_by_index(1)  # Deleting node at index 1
    print("\nLinked List after deleting a specific node by index:")
    Sll.print()
    print()

    # Clearing the linked list
    Sll.clear()
    print("\nLinked List after clearing:")
    Sll.print()  # Should print "SLL is Empty!"

