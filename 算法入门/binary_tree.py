# Zhaoyu Wang developed
# time: 2023-05-11 12:16 p.m.
class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

a = BinaryTree('A')
b = BinaryTree('B')
c = BinaryTree('C')
d = BinaryTree('D')
e = BinaryTree('E')
f = BinaryTree('F')
g = BinaryTree('G')

e.left = a
e.right = g
a.right = c
c.left = b
c.right = d
g.right = f

root = e
#           E
#       A       G
#         C       F
#       B   D
def pre_order(root):
    if root:
        print(root.data , end=', ')
        pre_order(root.left)
        pre_order(root.right)

def in_order(root):
    if root:
        pre_order(root.left)
        print(root.data, end=', ')
        pre_order(root.right)

def post_order(root):
    if root:
        pre_order(root.left)
        pre_order(root.right)
        print(root.data, end=', ')
pre_order(root)
print('\n')
in_order(root)
print('\n')
post_order(root)