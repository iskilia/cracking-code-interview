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


def delete_node(n: LinkedListNode) -> bool:
    if n is None or n.next is None:
        return False

    next = n.next
    n.val = next.val
    n.next = next.next
    return True


if __name__ == "__main__":
    head_node = build_list()
    node_to_delete = head_node.next.next
    delete_node(node_to_delete)
    curr_node = head_node
    while curr_node is not None:
        print(curr_node.val)
        curr_node = curr_node.next
