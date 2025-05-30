from linked_list_node import LinkedListNode


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = LinkedListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            assert self.tail is not None
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.head is None:
            return None

        previous = self.head
        current = self.head
        while current.next:
            previous = current
            current = current.next

        self.tail = previous
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return current

    def prepend(self, value):
        new_node = LinkedListNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
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
        if index < 0 or index >= self.length:
            return None

        node = self.head
        for _ in range(index):
            assert node is not None
            node = node.next
        return node

    def set(self, index: int, value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False

    def insert(self, index: int, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = LinkedListNode(value)
        temp = self.get(index - 1)
        if temp:
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True
        return False

    def remove(self, index: int):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        prev = self.get(index - 1)
        assert prev is not None
        toRemove = prev.next
        assert toRemove is not None
        prev.next = toRemove.next
        toRemove.next = None
        self.length -= 1

        return toRemove

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        assert temp is not None

        after = temp.next
        before = None
        for _ in range(self.length):
            assert temp is not None
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def print_list(self):
        node = self.head
        for _ in range(self.length):
            print(node)
            assert node is not None
            node = node.next
