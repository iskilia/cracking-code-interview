class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, next):
        self.next = next


def remove_duplicates_no_buffer(node: LinkedListNode):
    curr = node
    while curr is not None:
        runner = curr
        while runner.next != None:
            if runner.next.val == curr.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        curr = curr.next
    return


def remove_duplicates(node: LinkedListNode):
    my_set = set()
    prev: LinkedListNode = None
    while (node != None):
        if node.val in my_set:
            prev.next = node.next
        else:
            my_set.add(node.val)
            prev = node
        node = node.next
    return


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


def print_list(node: LinkedListNode):
    while node is not None:
        print(node.val)
        node = node.next


if __name__ == "__main__":
    first_list = build_list()
    second_list = build_list()
    remove_duplicates(first_list)
    remove_duplicates_no_buffer(second_list)
    print_list(first_list)
    print_list(second_list)
