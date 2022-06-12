from typing import Type

class Stack:

	elements = []

	count = -1

	def push(self, data):
		self.elements.append(data)
		self.count += 1

	def pop(self) -> int:
		if self.isEmpty() is True:
			raise Exception('Nothing to pop!')
		
		self.count -= 1
		self.elements.pop()

	def peek(self):
		if self.isEmpty() is True:
			raise Exception('Cannot peek an empty stack')

		return self.elements[self.count]

	def isEmpty(self):
		return self.count < 0

stack = Stack()
print(stack.isEmpty())

stack.push(1)
stack.push(2)

print(stack.peek())

stack.pop()
stack.pop()

print(stack.isEmpty())

try:
	stack.pop()
except:
	print('Cannot pop now as it is empty\n')

print("""*Stack*

- Stack is a LIFO based data structure. (Last In First Out)

- Time Complexity: For the array-based implementation of a stack, the push and pop operations take constant time, i.e. O(1).

Applications:
- To reverse a word
- The browser Back button uses this data structure to keep track of a tab's history
- In compilers - Compilers use the stack to calculate the value of expressions like 2 + 4 / 5 * (7 - 9).
""")