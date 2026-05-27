class BstNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left: BstNode | None = None
        self.right: BstNode | None = None
