from linked_list import LinkedList
from linked_list_node import LinkedListNode


def has_loop(linked_list: LinkedList):
    slow = linked_list.head
    fast = linked_list.head

    while fast is not None and fast.next is not None:
        assert slow is LinkedListNode
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False
