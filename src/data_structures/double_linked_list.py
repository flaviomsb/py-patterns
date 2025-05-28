from doubly_linked_list_node import DoublyLinkedListNode

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = DoublyLinkedListNode(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            assert self.tail is DoublyLinkedListNode
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = DoublyLinkedListNode(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop(self):
        if self.head is None:
            return None

        assert self.tail is DoublyLinkedListNode
        node = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
            node.previous = None
        self.length -= 1

        return node
