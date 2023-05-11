# Zhaoyu Wang developed
# time: 2023-05-11 8:53 a.m.
class Node:
    def __init__(self, item:int):
        self.item = item
        self.next = None

def create_ll_head(li:list[int]):

    head = Node(li[0])
    for element in li[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head

def create_ll_tail(li:list[int]):
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head

def print_ll(ll):
    while ll:
        print(ll.item, end=', ' )
        ll = ll.next
a = [1,2,3,4,5]
h = create_ll_tail(a)
print_ll(h)
