from data_structures.stack_list import StackList

def reverse_string(val: str) -> str:
    stack = StackList()
    reversed_string = ""
 
    for char in val:
        stack.push(char)
 
    while not stack.is_empty():
        char: str = str(stack.pop())
        reversed_string += char
 
    return reversed_string
