class Node:
    def __init__(self,data):
        self.data = data
        self.next =  None

class Queue:
        
    def __init__(self):

        self.rear = None
        self.front = None
        self.count = 0

    def enqueue(self,data):
        new_node = Node(data)

            # queue is empty                # front → [1] → [2] → [3] → None   : front is stay 1st only
                                            # rear -------------───^           only rear is trverses 

        if self.rear is None:
            self.front = new_node
            # self.rear = new_node
        
        else:
            self.rear.next = new_node
            # self.rear = new_node

        self.rear = new_node
        self.count += 1
        print(f"element {data} is inserted in queue")

    def dequeue(self):
        # queue is empty
        if self.front is None:
            print("queue is empty")
            return -100
        
        return_data = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self.count -= 1
        print(f"Removing element {return_data} from the queue")
        return return_data
    
    def peek(self) -> int:

        if self.front is None:
            print("queue is empty")
            return -100
        
        print("peek is", self.front.data)
        return self.front.data
    
    def get_count(self) -> int:
        print("count is ",self.count)
        return self.count 
    
    def print_all_nodes(self):

        if self.front is None:
            print("queue is empty")
            return -100
        
        print("the queue elements are ")
        current_node = self.front

        while current_node is not None:
            print(current_node.data, end = " -> ")
            current_node = current_node.next
        
        print("None")
        

que = Queue()
que.dequeue()
que.print_all_nodes()

que.enqueue(1)
que.print_all_nodes()
que.dequeue()
que.print_all_nodes()

que.enqueue(1)
que.enqueue(2)
que.enqueue(3)

que.print_all_nodes()
que.get_count()
que.peek()
que.dequeue()
que.print_all_nodes()



        
            