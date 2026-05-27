from bst_node import BstNode

class BinarySearchTree:
    def __init__(self) -> None:
        self.root: BstNode | None = None

    def insert(self, value):
        new_node = BstNode(value)

        if self.root is None:
            self.root = new_node
            return True

        temp = self.root
        while (True):
            # if new value is equals to current value
            # do not insert and return false
            if new_node.value == temp.value:
                return False

            # if new value is less than current node
            # then go to the left
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            # otherwise if greater than, then go to the right
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value) -> bool:
        temp = self.root
        while (temp is not None):
            if temp.value == value:
                return True

            if value < temp.value:
                temp = temp.left
            else:
                temp = temp.right

        return False
