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
 
    # Deletes the first node in the list
    def delete_at_beginning(self):              # Deletes the first node in the list
        if self.head is None:                   # if head is None, list is empty  
            print("list is empty")              
            return
        
        self.head = self.head.next              # move head to the next node, effectively deleting the first node
            

    # Deletes the last node in the list
    def delete_at_end(self):                               # Deletes the last node in the list
        if self.head is None:                              # if head is None, list is empty
            print("list is empty")
            return
        
        if self.head.next is None:                         # if there is only one node
            self.head = None                               # effectively deleting the only node
            return

        current_node = self.head                           # start from head/currently in head node

        while current_node.next.next is not None:          # traverse to the second last node
            current_node = current_node.next               # move to the next node
            
        current_node.next   = None                  # set the next of the second last node to None, effectively deleting the last node


    # Deletes a node at a specific position
    def delete_at_position(self,del_position):          # Deletes a node at a specific position

        if del_position <= 0 :                          # if position is less than or equal to 0, it's invalid    
            print("invalid position")
            return
        
        if del_position == 1:                           # if position is 1, delete the first node

            if self.head is None:                       # if head is None, list is empty
                print("list is empty")
                return

            self.head = self.head.next               # move head to the next node, effectively deleting the first node
            return

        current_node = self.head                        # start from head/currently in head node
        current_position = 1                            # initialize current position to 1

        while current_position < del_position - 1 and current_node is not None:     # traverse to the node before the one to be deleted
            current_position += 1                                                   # increment current position
            current_node = current_node.next                                        # move to the next node

        if current_node is None or current_node.next is None:           # if current_node is None or next node is None, position is out of bounds
            print("out of the position")
            return

        current_node.next = current_node.next.next                      # set the next of the current node to the node after the one to be deleted, effectively deleting the node at del_position

        

 # driver code to test the above class
if __name__ == "__main__":
    sll = SinglyLinkedList()

    # Insert at beginning
    sll.insert_at_beginning(10)  # list: 10 -> None
    sll.insert_at_beginning(20)
    sll.insert_at_beginning(30)  # list: 20 -> 10 -> None
    sll.insert_at_beginning(40)  # list: 30 -> 20 -> 10 -> None
    sll.insert_at_beginning(50)  # list: 40 -> 30 -> 20 -> 10 -> None
    sll.insert_at_beginning(60)  # list: 50 -> 40 -> 30 -> 20 -> 10 -> None
    sll.print_list()             # print the list

    sll.delete_at_beginning() 
    sll.print_list()
    sll.delete_at_end()          # Deletes 10
    sll.print_list()
    sll.delete_at_position(2)    # Deletes 20
    sll.print_list()