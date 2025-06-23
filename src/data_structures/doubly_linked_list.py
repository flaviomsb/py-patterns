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

    def set_at(self, index, value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False

    def insert_at(self, index, value):
        if index < 0 or index > self.length:
            return False

        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        new_node = DoublyLinkedListNode(value)
        before = self.get(index - 1)
        assert before is DoublyLinkedListNode
        after = before.next
        new_node.previous = before
        new_node.next = after
        before.next = new_node
        after.previous = new_node
        self.length += 1

        return True

    def remove_at(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        node = self.get(index)
        assert node is DoublyLinkedListNode
        node.previous.next = node.next
        node.next.previous = node.previous
        node.previous = None
        node.next = None
        self.length -= 1
        return node

    def is_palindrome(self):
        if self.length <= 1:
            return True

        forward_node = self.head
        backward_node = self.tail
        assert forward_node and backward_node is DoublyLinkedListNode
        for _ in range(self.length // 2):
            if forward_node.value != backward_node.value:
                return False
            forward_node.next
            backward_node.previous
        return True
