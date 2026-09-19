class Node:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.next = None

class serviceQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.queue_count = 0

    def accept_orders(self, element):
        new_node = Node(element)
        if self.front is None:
            self.front = self.rear = new_node
            self.queue_count += 1
            return
        self.rear.next = new_node
        self.rear = new_node
        self.queue_count += 1

    def fill_the_order