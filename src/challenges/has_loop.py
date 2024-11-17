from data_structures import LinkedList

def has_loop(linked_list: LinkedList):
    slow = linked_list.head
    fast = linked_list.head

    while(fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False
