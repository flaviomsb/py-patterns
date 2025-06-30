from data_structures.linked_list_node import LinkedListNode

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.legth = 0
    
    def enqueue(self, value):
        new_node = LinkedListNode(value)

        if self.legth == 0:
            self.first = new_node
            self.last = new_node
        else:
            assert self.last is LinkedListNode
            self.last.next = new_node
            self.last = new_node
        self.legth += 1
