class Stack:
    stack = []
    top = -1

    def push(self, n):
        self.stack.append(n)
        self.top = self.stack[len(self.stack) - 1]

    def pop(self):
        if len(self.stack) == 0:
            return 'Stack underflow'
        elif len(self.stack) == 1:
            self.top = -1
            return self.stack.pop()
        else:
            self.top = self.stack[len(self.stack) - 2]
            return self.stack.pop()

    def peep(self):
        if len(self.stack) == 0:
            return 'Stack is empty'
        else:
            return self.top

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
