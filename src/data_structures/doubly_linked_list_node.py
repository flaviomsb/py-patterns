class DoublyLinkedListNode:
    def __init__(self, value) -> None:
        self.value = value
        self.next: DoublyLinkedListNode | None = None
        self.previous: DoublyLinkedListNode | None = None

