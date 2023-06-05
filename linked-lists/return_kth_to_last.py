class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, next):
        self.next = next


def build_list() -> LinkedListNode:
    root_node = LinkedListNode(0)
    first_node = LinkedListNode(1)
    second_node = LinkedListNode(1)
    third_node = LinkedListNode(2)
    fourth_node = LinkedListNode(3)
    root_node.set_next(first_node)
    first_node.set_next(second_node)
    second_node.set_next(third_node)
    third_node.set_next(fourth_node)
    return root_node


def nth_to_last(head: LinkedListNode, k: int) -> LinkedListNode:
    p1 = head
    p2 = head

    for _ in range(k):
        if p1 is None:
            return None
        p1 = p1.next

    while p1 is not None:
        p1 = p1.next
        p2 = p2.next

    return p2


if __name__ == "__main__":
    my_list = build_list()
    nth_to_last_node = nth_to_last(my_list, 2)
    print(nth_to_last_node.val)
