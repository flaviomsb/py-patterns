from linked_list import LinkedList


def find_middle_node(linked_list: LinkedList):
    slow = linked_list.head
    fast = linked_list.head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow
