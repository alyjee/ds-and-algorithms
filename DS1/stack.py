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
	print('Cannot pop now as it is empty')