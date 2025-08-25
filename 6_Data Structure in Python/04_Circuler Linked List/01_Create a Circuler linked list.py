class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CLL:
    def __init__(self):
        self.tail = None

    def insert_at_beginning(self,data):
        new_node = Node(data)

        # empty list
        if self.tail is None:
            self.tail = new_node
            new_node.next = new_node
            return
        # 1 or 2 or more nodes
        new_node.next = self.tail.next
        self.tail.next = new_node

    def print_list(self):
        if self.tail is None:
            print("list is empty")
            return

        current_node = self.tail.next
        while True:
            print(current_node.data, end = "->")
            current_node = current_node.next
            if current_node == self.tail.next:  # stop when back to head
                break
        print("(head)")
        

cll = CLL()
cll.insert_at_beginning(10)
cll.insert_at_beginning(20)
cll.insert_at_beginning(30)
cll.print_list()