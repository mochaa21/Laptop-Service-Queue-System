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

    def fill_the_order(self):
        if self.isEmpty():
            return "No orders"
        temp = self.front
        self.front = temp.next
        self.queue_count -= 1
        if self.front is None:
            self.rear = None
        return temp.data

    def first_order(self):
        if self.isEmpty():
            return "No orders"
        return self.front.data

    def isEmpty(self):
        return self.queue_count == 0

    def view_queue(self):
        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print()

workshop = serviceQueue()

workshop.accept_orders("Client A (Asus ROG)")
workshop.accept_orders("Client B (Lenovo Thinkpad)")
workshop.accept_orders("Client C (Acer Nitro)")

print("Entry queue list:")
workshop.view_queue()

print("Start working on:", workshop.fill_the_order())
print("Start working on:", workshop.fill_the_order())