from data_structures.linked_list_node import LinkedListNode

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    
    def enqueue(self, value):
        new_node = LinkedListNode(value)

        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            assert self.last is LinkedListNode
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None

        assert self.first is LinkedListNode
        node = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            node.next = None
        self.length -= 1

        return node
