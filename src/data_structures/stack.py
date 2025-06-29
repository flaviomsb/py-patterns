from data_structures.linked_list_node import LinkedListNode

class Stack:
    def __init__(self, value) -> None:
        self.top = LinkedListNode(value)
        self.height = 1
