from stack import Stack
from student import Student
from custom_queue import Queue

my_stack = Stack()
my_stack.push("Mac")
my_stack.push("Charlie")
my_stack.push("Dee")
my_stack.push("Denis")
my_stack.push("Frank")
my_stack.push("Joe")
my_stack.push("jill")

print(my_stack)

my_stack.pop()

print(my_stack)

stu_stack = Stack()

stu_stack.push(Student("Alice", 3.5))
stu_stack.push(Student("Bob", 2.0))

print(stu_stack)

my_queue = Queue()

my_queue.enqueue("Alice")
my_queue.enqueue("Bob")
my_queue.enqueue("Charlie")

print(my_queue)

my_queue.dequeue()

print(my_queue)

