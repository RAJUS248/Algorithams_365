class  Node:
       def __init__(self, data):
              self.data = data
              self.next = None

class SinglyLinkedList:
       def __init__(self):
              self.head = None

              # Insert a new node at a specific position

       def insert_at_position(self, position, data):
              
              # Invalid position

              if position < 1:
                     print("Invalid")     
                     return               
              
              
              new_node = Node(data)                            # Create a new node with the given data

               # Case 1: Insert at beginning
              if position == 1:                                # If inserting at the head
                     new_node.next = self.head                 # Point new node to current head
                     self.head = new_node                      # Update head to new node
                     return
              
              # Case 2: Insert at position greater than 1
              current_node = self.head
              current_position = 1

              while current_position < position - 1 and current_node is not None:
                     current_node = current_node.next
                     current_position += 1

                           # Link the previous node to the new node

              # If current_node is None, it means the position is invalid
              if current_node is None:                    
                     print(f"{position} is Invalid position")
                     return
              
              new_node.next = current_node.next         # Point new node to the next node
              current_node.next = new_node 
              
              
              
       def print_list(self):
              current_node = self.head
              while current_node is not None:
                     print(current_node.data, end=" -> ")
                     current_node = current_node.next
              print("None")

sll = SinglyLinkedList()
# Example usage
sll.insert_at_position(1, 10)  # Insert 10 at position
sll.insert_at_position(2, 20)  # Insert 20 at position 2
sll.insert_at_position(3, 30)  # Insert 30 at position 3

sll.print_list()                   # Print the list: 10 -> 15 -> 20 -> 30 -> None
sll.insert_at_position(2, 40)      # Insert 40 at position 5
sll.insert_at_position(6, 15)      # Insert 15 at position 2
sll.print_list()                   # Print the list: 10 -> 15 -> 40 -> 20 -> 30 -> None

       