from data_structures.stack_list import StackList

def is_balanced_parentheses(parentheses: str) -> bool:
    stack = StackList()
    for p in parentheses:
        if p == "(":
            stack.push(p)
        elif p == ")":
            if stack.is_empty() or stack.pop() != "(":
                return False
    return stack.is_empty()
