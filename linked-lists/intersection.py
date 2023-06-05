class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, next):
        self.next = next


class Result:
    def __init__(self, tail: LinkedListNode, size: int):
        self.tail = tail
        self.size = size


def print_list(head: LinkedListNode):
    curr = head
    while curr is not None:
        print(curr.val)
        curr = curr.next


def build_list():
    root_node = LinkedListNode(1)
    second_node = LinkedListNode(2)
    third_node = LinkedListNode(5)
    fourth_node = LinkedListNode(1)
    root_node_2 = LinkedListNode(1)
    second_node_2 = LinkedListNode(3)
    root_node_2.set_next(second_node_2)
    second_node_2.set_next(third_node)
    root_node.set_next(second_node)
    second_node.set_next(third_node)
    third_node.set_next(fourth_node)
    return root_node, root_node_2


def get_tail_and_size(list: LinkedListNode) -> Result:
    if list is None:
        return None
    size = 1
    curr = list
    while curr is not None:
        size += 1
        curr = curr.next

    return Result(curr, size)


def get_kth_node(head: LinkedListNode, k: int) -> LinkedListNode:
    curr = head
    while (k > 0 and curr is not None):
        curr = curr.next
        k -= 1
    return curr


def find_intersection(l1: LinkedListNode, l2: LinkedListNode) -> LinkedListNode:
    if l1 is None or l2 is None:
        return None
    res1 = get_tail_and_size(l1)
    res2 = get_tail_and_size(l2)
    if res1.tail is not res2.tail:
        return None

    shorter = l1 if res1.size < res2.size else l2
    longer = l2 if res1.size < res2.size else l1

    longer = get_kth_node(longer, abs(res1.size - res2.size))

    while shorter != longer:
        shorter = shorter.next
        longer = longer.next

    return longer


if __name__ == "__main__":
    l1, l2 = build_list()
    intersection = find_intersection(l1, l2)
    print(intersection.val)
