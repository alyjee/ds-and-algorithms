# Linked List

class LinkedList:

	def __init__(self, head=None):
		self.head = None

class Node:
	def __init__(self, data, next=None):
		self.data = data
		self.next = next


def createFromArray(nodeList):

	ll = LinkedList()

	prev = None
	for n in nums:
		curr = Node(n)

		if not prev:
			ll.head = curr
		else:
			prev.next = curr

		prev = curr

	return ll

# Make linked-list from array - O(n)
nums = [1,2,3,4,5]
ll = createFromArray(nums)

def traverseList(ll):
	curr = ll.head

	while curr:
		print(curr.data, end=" -> ")
		curr = curr.next

# traverse a linked-list O(n)
traverseList(ll)













