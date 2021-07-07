class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def __repr__(self):
        return repr(self.data)
    def add_left(self,node):
        self.left=node
    def add_right(self,node):
        self.right=node
"""
			-2-
		   /   \
		  7     9
		 / \     \
		1   6     8
		   / \   / \
		  5  10 3   4
"""
def create_tree():
    two=Node(2)
    seven=Node(7)
    nine=Node(9)
    two.add_left(seven)
    two.add_right(nine)
    one=Node(1)
    six=Node(6)
    eight=Node(8)
    seven.add_left(one)
    seven.add_right(six)
    nine.add_right(eight)
    five=Node(5)
    ten=Node(10)
    three=Node(3)
    four=Node(4)
    six.add_left(five)
    six.add_right(ten)
    eight.add_left(three)
    eight.add_right(four)
    
    return two
    
def post_order(node):
    if node.left:
        post_order(node.left)
    if node.right:
        post_order(node.right)
    print(node)
    
if __name__=="__main__":
    root=create_tree()
    post_order(root)