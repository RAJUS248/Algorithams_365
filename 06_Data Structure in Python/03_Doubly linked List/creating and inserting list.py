class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        new_node = Node(data)

        # list is empty
        if self.head is None:
            self.head = new_node
            return
        
        
        # 1 or more nodes
        new_node.next = self.head       # new_node.next -> head
        self.head.prev = new_node       # head.prev -> new_node
        self.head = new_node            # self.head -> new_node

    def insert_at_end(self,data):
        new_node = Node(data)

        # list is empty
        if self.head is None:
            self.head = new_node
            return
        
        # for 1 node only
        if self.head.next is None:
            self.head.next = new_node
            new_node.prev = self.head
            return
        
        # 2 or more nodes
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node
        new_node.prev = current_node


        
    def print_list(self):
        
        current_node = self.head

        while current_node is not None:
            print(current_node.data , end = " <-> ")
            current_node = current_node.next

        print("None")

# driver code to test the above class
def insert_at_beginning_test():

    dll = DoublyLinkedList()
    dll.insert_at_beginning(10)
    dll.insert_at_beginning(20)

    dll.print_list()

def insert_at_end_test():
    dll = DoublyLinkedList()
    dll.insert_at_end(10)
    dll.insert_at_end(20)
    dll.insert_at_end(30)

    dll.print_list()
if __name__ == "__main__":

    # insert_at_beginning_test() 
    insert_at_end_test()
    