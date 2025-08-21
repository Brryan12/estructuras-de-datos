class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None  # Points to next node
        self.prev = None  # Points to previous node

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = DoubleNode(value)
        if self.head is None:  # Empty list
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def display_forward(self):
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            last = current
            current = current.next
        print("None")

    def display_backward(self):
        # Go to the last node
        current = self.head
        if current is None:
            print("None")
            return
        while current.next:
            current = current.next
        # Traverse backwards
        while current:
            print(current.value, end=" <-> ")
            current = current.prev
        print("None")

    def eliminar(self, value):
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:  # If head is to be removed
                    self.head = current.next
                print(f"Removed: {value}")
                return
            current = current.next
        print(f"Value {value} not found.")

# Example
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.display_forward()   # 10 <-> 20 <-> 30 <-> None
dll.display_backward()  # 30 <-> 20 <-> 10 <-> None
dll.eliminar(20)       # Removes 20
dll.display_forward()   # 10 <-> 30 <-> None

