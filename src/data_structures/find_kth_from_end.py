from data_structures import LinkedList

def find_kth_from_end(linked_list: LinkedList, kth: int):
    slow = linked_list.head
    fast = linked_list.head

    for _ in range(kth):
        if fast is None:
            return None
        fast = fast.next

    while(fast is not None):
        slow = slow.next
        fast = fast.next

    return slow


