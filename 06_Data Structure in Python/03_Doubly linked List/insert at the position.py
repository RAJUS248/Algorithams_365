class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None

    def insert_at_position(self,ur_position,data):
        new_node = Node(data)
        
        #insert at start
        if ur_position == 1:
            if self.head is not None:
                new_node.next = self.head
                self.head.prev = new_node
            self.head = new_node
            return
        

        # 2 or more node
        current_node = self.head
        position = 1

        while current_node is not None and position < ur_position - 1:
            current_node = current_node.next
            position += 1

        if current_node is None:
            print("invalid postion")
            return
        
        new_node.next = current_node.next
        if current_node.next is not None:
            current_node.next.prev = new_node
        
        current_node.next = new_node
        new_node.prev = current_node

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end = " <-> ")
            current_node = current_node.next
        
        print("None")

    def rverse_print(self):
        current_node = self.head

        if self.head is None:
            print("list is empty")
            return
        
        while current_node.next is not None:
            current_node = current_node.next
            
        while current_node is not None:
            print(current_node.data, end = " <-> ")
            current_node = current_node.prev

        print("None")

        

dll = DLL()

dll.print_list()
dll.insert_at_position(1,10)
dll.insert_at_position(2,20)
dll.insert_at_position(2,50)
dll.insert_at_position(3,30)
dll.insert_at_position(4,40)

dll.print_list()
dll.rverse_print()


