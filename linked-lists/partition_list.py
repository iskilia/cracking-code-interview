class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, next):
        self.next = next


def build_list() -> LinkedListNode:
    root_node = LinkedListNode(0)
    first_node = LinkedListNode(1)
    second_node = LinkedListNode(2)
    third_node = LinkedListNode(1)
    fourth_node = LinkedListNode(3)
    fifth_node = LinkedListNode(5)
    sixth_node = LinkedListNode(3)
    root_node.set_next(first_node)
    first_node.set_next(second_node)
    second_node.set_next(third_node)
    third_node.set_next(fourth_node)
    fourth_node.set_next(fifth_node)
    fifth_node.set_next(sixth_node)
    return root_node


def partition(node: LinkedListNode, x: int) -> LinkedListNode:
    head = node
    tail = node

    while (node is not None):
        next = node.next
        if node.val < x:
            node.next = head
            head = node
        else:
            tail.next = node
            tail = node
        node = next

    return head


if __name__ == "__main__":
    head_node = build_list()
    new_list = partition(head_node, 3)
    curr = new_list
    while curr is not None:
        print(curr.val)
        curr = curr.next
