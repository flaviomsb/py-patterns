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

    def pop_first(self):
        if self.head is None:
            return None

        node = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = node.next
            assert self.head is DoublyLinkedListNode
            self.head.previous = None
            node.next = None
        self.length -= 1

        return node

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        node = self.head
        # if index is in the first half of list
        if index < self.length / 2:
            for _ in range(index):
                assert node is DoublyLinkedListNode
                node = node.next
        # else if index is closer to the tail (second half of the list) 
        else:
            node = self.tail
            for _ in range(self.length - 1, index, -1):
                assert node is DoublyLinkedListNode
                node = node.previous

        return node
