class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class DLL:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def delete_at_beginning(self):
        # list empty
        if self.head is None:
            print("list is empty")
            return
        
        # one node
        if self.head.next is None:
            self.head = None
            return
        
        # 2 or more nodes
        
        self.head = self.head.next
        self.head.prev = None
            
        
    def delete_at_end(self):
        # list empty
        if self.head is None:
            print("list is empty")
            return
        # one Node
        if self.head.next is None:
            self.head = None
            return
        
        # 2 or more nodes
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.prev.next = None


    def print_list(self):
        
        current_node = self.head

        while current_node is not None:
            print(current_node.data , end = " <-> ")
            current_node = current_node.next

        print("None")

    def search(self,key):

        if self.head is None:
            print("list is empty")
            return
        
        current_node = self.head
        while current_node is not None:
            if current_node.data == key:
                print(f"key {key} found")
                return
            current_node = current_node.next

        print(f"key {key} not found")
        

dll = DLL()

dll.insert_at_beginning(50)

dll.insert_at_beginning(40)
dll.insert_at_beginning(30)
dll.insert_at_beginning(20)
dll.insert_at_beginning(10)

dll.print_list()
dll.search(10)

dll.delete_at_beginning()
dll.print_list()
dll.search(10)
dll.delete_at_end()
dll.print_list()
dll.search(10)


