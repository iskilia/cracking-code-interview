class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, next):
        self.next = next


class PartialSum:
    def __init__(self):
        self.sum = None
        self.carry = 0


def print_list(head: LinkedListNode):
    curr = head
    while curr is not None:
        print(curr.val)
        curr = curr.next


def insert_before(list: LinkedListNode, data: int) -> LinkedListNode:
    new_node = LinkedListNode(data)
    if list is not None:
        new_node.next = list
    return new_node


def pad_list(n: LinkedListNode, padding: int) -> LinkedListNode:
    head = n
    for _ in range(padding):
        head = insert_before(head, 0)
    return head


def length(n: LinkedListNode):
    count = 0
    while n is not None:
        count += 1
        n = n.next
    return count


def add_lists_helper(l1: LinkedListNode, l2: LinkedListNode) -> PartialSum:
    if l1 is None and l2 is None:
        ret_sum = PartialSum()
        return ret_sum

    ret_sum = add_lists_helper(l1.next, l2.next)

    new_val = ret_sum.carry + l1.val + l2.val
    full_result = insert_before(ret_sum.sum, int(new_val % 10))

    ret_sum.sum = full_result
    ret_sum.carry = new_val / 10
    return ret_sum


def add_lists(l1: LinkedListNode, l2: LinkedListNode) -> LinkedListNode:
    len1 = length(l1)
    len2 = length(l2)

    if len1 < len2:
        l1 = pad_list(l1, len2 - len1)
    else:
        l2 = pad_list(l2, len1 - len2)

    sum = add_lists_helper(l1, l2)

    if sum.carry == 0:
        return sum.sum
    else:
        result = insert_before(sum.sum, int(sum.carry))
        return result


def get_digit(n: int, digit: int):
    return n // 10 ** digit % 10


def build_list(x: int) -> LinkedListNode:
    root_node = LinkedListNode(get_digit(x, 0))
    prev_node = root_node
    for i in range(1, len(str(x))):
        next_node = LinkedListNode(get_digit(x, i))
        prev_node.set_next(next_node)
        prev_node = next_node
    return root_node


if __name__ == "__main__":
    head_node = build_list(4321)
    head_node_2 = build_list(765)
    result = add_lists(head_node, head_node_2)
    print_list(result)
