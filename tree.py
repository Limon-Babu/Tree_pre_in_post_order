class Node:
	def __init__(self,data):
		self.data=data
		self.right=None
		self.left=None
		
	def __repr__(self):
		return repr(self.data)
	def add_right(self,node):
		self.right=node
	def add_left(self,node):
		self.left=node
			
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
	two.add_right(nine)
	two.add_left(seven)
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
	
if __name__=="__main__":
	root=create_tree()
	print(root)