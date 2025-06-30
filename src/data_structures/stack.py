from data_structures.linked_list_node import LinkedListNode

class Stack:
    def __init__(self, value) -> None:
        if value:
            self.push(value)

    def push(self, value):
        new_node = LinkedListNode(value)

        if self.top is None:
            self.top = new_node 
        else:
            current_top = self.top
            new_node.next = current_top
            self.top = new_node
        self.height += 1
