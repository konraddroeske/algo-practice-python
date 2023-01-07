class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" = None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode(val={self.val}, next={self.next})"
