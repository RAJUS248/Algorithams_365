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


    def delete_at_position(self,del_position):

        if del_position <= 0 :
            print("invalid position")
            return
        
        if del_position == 1:

            if self.head is None:
                print("list is empty")
                return

            self.head = self.head.next
            return

        current_node = self.head
        current_position = 1

        while current_position < del_position - 1 and current_node is not None:
            current_position += 1
            current_node = current_node.next

        if current_node is None or current_node.next is None:
            print("out of the position")
            return

        current_node.next = current_node.next.next

         

# driver code to test the above class
if __name__ == "__main__":
    sll = SinglyLinkedList()

    # Insert at beginning
    sll.insert_at_beginning(10)  # list: 10 -> None
    sll.insert_at_beginning(20)  # list: 20 -> 10 -> None
    sll.insert_at_beginning(30)  # list: 30 -> 20 -> 10 -> None
    
    sll.print_list()             # print the list

    sll.delete_at_position(1)    # Deletes 20
    sll.print_list()             # Should print: 10 -> None