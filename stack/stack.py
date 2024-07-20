import random

choices = ["stack", "queue", "heap"]
print(random.choice(choices))

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)


#use the class

new_stack = Stack()

# add items to the stack
new_stack.push("banana")
new_stack.push("apple")
new_stack.push("watermelon")

# remove an item from the stack
print(new_stack.pop()) #removes watermelon

print(new_stack.peek()) #returns apple

print(new_stack.is_empty()) # returns false

print(new_stack.size()) # returns 2
