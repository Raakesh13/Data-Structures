class Queue:
    queue = []
    front = -1
    rare = -1

    def enQueue(self, n):
        if len(self.queue) == 0:
            self.queue.append(n)
            self.rare = self.queue[len(self.queue) - 1]
            self.front = self.queue[0]
        else:
            self.queue.append(n)
            self.rare = self.queue[len(self.queue) - 1]

    def deQueue(self):
        if len(self.queue) == 0:
            return 'Queue underflow'
        elif len(self.queue) == 1:
            self.rare = -1
            self.front = -1
            return self.queue.pop(0)
        else:
            self.front = self.queue[1]
            return self.queue.pop(0)

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
