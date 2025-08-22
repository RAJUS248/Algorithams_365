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


    def print_list(self):               # start from head/currently in head node
        current = self.head                 # current --> head

        while current:                          # while current is not None
            print(current.data, end=" -> ")     # print current node data ex: 10 ->
            current = current.next              # move to the next node
        print("None")                           # print None at the end of the list ex: 10 -> 20 -> None


    def delete_at_beginning(self):
        if self.head is None:                            # if head is None, list is empty
            print("List is empty, nothing to delete.")
            return
        self.head = self.head.next                       # move head to the next node, effectively deleting the first node   

# driver code to test the above class
if __name__ == "__main__":
    sll = SinglyLinkedList()

    # Insert at beginning
    sll.insert_at_beginning(10)  # list: 10 -> None
    sll.insert_at_beginning(20)  # list: 20 -> 10 -> None
    sll.print_list()             # print the list

    sll.delete_at_beginning()    # Deletes 20
    sll.print_list()             # Should print: 10 -> None