class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, next):
        self.next = next


def print_list(head: LinkedListNode):
    curr = head
    while curr is not None:
        print(curr.val)
        curr = curr.next


def build_list():
    root_node = LinkedListNode(1)
    second_node = LinkedListNode(2)
    third_node = LinkedListNode(2)
    fourth_node = LinkedListNode(1)
    root_node.set_next(second_node)
    second_node.set_next(third_node)
    third_node.set_next(fourth_node)
    return root_node


def is_palindrome(head: LinkedListNode) -> bool:
    fast = head
    slow = head
    stack = []

    while fast is not None and fast.next is not None:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next

    if fast is not None:
        slow = slow.next

    while slow is not None:
        top = stack.pop()
        if top is not slow.val:
            return False
        slow = slow.next
    return True


if __name__ == "__main__":
    head_node = build_list()
    is_pal = is_palindrome(head_node)
    print(is_pal)
