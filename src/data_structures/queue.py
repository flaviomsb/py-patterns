from data_structures.linked_list_node import LinkedListNode

class Queue:
    def __init__(self, value):
        new_node = LinkedListNode(value)
        self.first = new_node
        self.last = new_node
        self.legth = 1
    
    
