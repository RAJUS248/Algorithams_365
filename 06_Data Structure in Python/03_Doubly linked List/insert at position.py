class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None

    def insert_at_position(self, data, position):

        new_node = Node(data)

        # 1. Position ≤ 0

        if position <= 0:
            print(f"{position} is invalid Position ")
            return
        
        # 2. Insert at beginning (position = 1)

        if position == 1:
            new_node.next = self.head      # new node points to old head            new_node.next -> head
            if self.head:                  # if list is not empty                   
                self.head.prev = new_node  # old head's prev points to new node     head.prev -> new_node
            self.head = new_node           # update head to new node                head -> new_node
            return

        # 3. Traverse to node before target

        current_node = self.head
        target_position = 1

        while current_node is not None and target_position < position -1:
            current_node = current_node.next
            target_position += 1

        # 4. Invalid (position beyond length)

        if current_node is None:
            print("invalid position beyond length ")
            return
        
        # Insert at the end if current.next is None

        if current_node.next is None:
            current_node.next = new_node
            new_node.prev = current_node
            return
        
        # Insert in the middle

        new_node.next = current_node.next
        new_node.prev = current_node
        current_node.next.prev = new_node
        current_node.next = new_node
        
    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
        print("None")

dll = DLL()
dll = DLL()
dll.insert_at_position(10, 2)  # invalid (list empty, only pos=1 is valid)
dll.insert_at_position(20, 1)  # insert at beginning
dll.insert_at_position(30, 2)  # insert at position 2 (middle/end case)
dll.insert_at_position(40, 3)  # insert in middle
dll.insert_at_position(50, 4)  # insert at end
dll.insert_at_position(60, 10) # invalid (too large)
dll.insert_at_position(70, 0)  # invalid (position ≤ 0)

dll.print_list()