from ll_node import LLNode

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = LLNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.head is None:
            return None

        previous = self.head
        current = self.head
        while (current.next):
            previous = current
            current = current.next

        self.tail = previous
        self.tail.next = None
        self.length -= 1

        if self.length is 0:
            self.head = None
            self.tail = None

        return current

    def prepend(self, value):
        new_node = LLNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
        return True

    def pop_first(self):
        if self.head is None:
            return None

        node = self.head
        self.head = self.head.next
        node.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return node

    def get(self, index: int):
        if index == 0 or index >= self.length:
            return None

        node = self.head
        for _ in range(index):
            node = node.next
        return node

    def set(self, index: int, value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False
