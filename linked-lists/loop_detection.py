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
    root_node = LinkedListNode(0)
    prev_node = root_node
    for i in range(1, 100):
        new_node = LinkedListNode(i)
        prev_node.set_next(new_node)
        prev_node = new_node
    curr_node = root_node
    for i in range(0, 20):
        curr_node = curr_node.next
    prev_node.set_next(curr_node)
    return root_node


def find_beginning(head: LinkedListNode) -> LinkedListNode:
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if fast is None or fast.next is None:
        return None
    slow = head
    while slow is not fast:
        slow = slow.next
        fast = fast.next
    return fast


if __name__ == "__main__":
    head = build_list()
    loop_beginning = find_beginning(head)
    print(loop_beginning.val)
