class Node:                             # class which represent the node in singly linked list
    def __init__(self, data):

        self.data =  data               # Store data
        self.next = None                # Initialize next as None   

class SinglyLinkedList:
    def __init__(self):
        self.head = None                # head is the first node in the linked list
        
    def insert_at_beginning(self, data):       # creating new node 
        new_node = Node(data)                  # newNode --> data| next
        new_node.next = self.head              # next --> head
        self.head = new_node                   # head --> newNode


    def print_list(self):                   # start from head/currently in head node
        current = self.head                 # current --> head

        while current:                          # while current is not None
            print(current.data, end=" -> ")     # print current node data ex: 10 ->
            current = current.next              # move to the next node
        print("None")                           # print None at the end of the list ex: 10 -> 20 -> None

    def search(self, key):

        # when list is empty
        if self.head is None:
            print("List is empty, nothing to search.")          
            return
        
        # start from head/currently in head node
        current_node = self.head

        # traverse the list to find the key
        while current_node is not None:
            if current_node.data == key:
                print(f"Value {key} found in the list.")
                return 
            current_node = current_node.next

        print(f"Value {key} not found in the list.")

def search_driver_code(sll:SinglyLinkedList):
        sll.insert_at_beginning(13)
        sll.insert_at_beginning(20)
        sll.insert_at_beginning(10)  
        sll.print_list()                   # Should print: 10 -> 20 -> 13 -> None
        sll.search(10)                     # Should find 10
        sll.search(20)                     # Should find 20    
        sll.search(30)                     # Should not find 30
         

 
# driver code to test the above class
if __name__ == "__main__":
    sll = SinglyLinkedList()

    search_driver_code(sll)       # Test search functionality
               
    

    