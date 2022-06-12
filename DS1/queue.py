class Queue:
	elements = []
	front = -1
	rear = -1

	def enqueue(self, data):
		self.elements.append(data)
		if self.isEmpty():
			self.reset()
			self.front += 1

		self.rear += 1

	def dequeue(self):
		if self.isEmpty():
			raise Exception('Nothing to dequeue!')

		element = self.elements[self.front]
		self.front += 1

		return element

	def isEmpty(self):
		if self.front == self.rear == -1 or self.front > self.rear:
			return True

		return False

	def count(self):
		return self.front - self.rear + 1

	def reset(self):
		self.front = self.rear = -1

queue = Queue()

print(queue.isEmpty())

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

print(queue.isEmpty())

queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()

print(queue.isEmpty())

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.isEmpty())

queue.dequeue()
queue.dequeue()
queue.dequeue()

print(queue.isEmpty())

print("""*Queue*

- Queue is a FIFO based data structure. (First In First Out)

- Time Complexity: The complexity of enqueue and dequeue operations in a queue using an array is O(1) but if you use pop() in Python the complexity might be O(n) depending on the position of the item to be popped.

Applications:
- Call Center phone systems use Queues to hold people calling them in order.
- CPU scheduling, Disk Scheduling
- When data is transferred asynchronously between two processes.The queue is used for synchronization. For example: IO Buffers, pipes, file IO, etc
""")