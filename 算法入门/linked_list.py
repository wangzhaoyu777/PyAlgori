# Zhaoyu Wang developed
# time: 2023-05-11 8:53 a.m.
class Node:
    def __init__(self, item:int):
        self.item = item            #
        self.next = None

def create_ll_head(li:list[int]):   # add node before head
    head = Node(li[0])              # create the very first node is head
    for element in li[1:]:          # iterate elements in the list, after the first item
        node = Node(element)        # create a node
        node.next = head            # make the node point to the current head
        head = node                 # then make this node as the head
    return head                     # return head so that other item can be found

def create_ll_tail(li:list[int]):   # add node behind tail
    head = Node(li[0])              # same as former function
    tail = head                     # now we need a tail which is same as head at this moment,there is only one item
    for element in li[1:]:          # iterate element in list
        node = Node(element)        #
        tail.next = node            # tail point to the new node
        tail = node                 #
    return head

def print_ll(ll):
    while ll:
        print(ll.item, end=', ' )
        ll = ll.next
a = [1,2,3,4,5]
h = create_ll_tail(a)
print_ll(h)
