from data_structures.linked_list_node import LinkedListNode

class Stack:
    def __init__(self, value) -> None:
        self.top: LinkedListNode | None = None
        self.height = 0
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

    def pop(self):
        if self.height == 0:
            return None

        node = self.top
        assert node is LinkedListNode
        self.top = node.next
        node.next = None
        self.height -= 1

        return node
