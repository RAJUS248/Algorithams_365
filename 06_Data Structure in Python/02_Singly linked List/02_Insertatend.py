class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        new_node = Node(data)

        # check is list empty
        if self.head is None:
            self.head = new_node
            return

        # for 1 node
        if self.head.next is None:
            self.head.next = new_node
            return

        # for 2 or more nodes
        current_node = self.head
      
        while current_node.next is not None:
            current_node =  current_node.next 

        current_node.next  = new_node
        return
        

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# driver code to test the above class
if __name__ == "__main__":
    sll = SinglyLinkedList()

    # Insert at end
    sll.insert_at_end(10)  # list: 10 -> None
    sll.insert_at_end(20)  # list: 10 -> 20 -> None
    sll.insert_at_end(30)  # list: 10 -> 20 -> 30 -> None
    sll.print_list()       # print the list




        