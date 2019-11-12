class Node:

    def __init__(self):
        self.data = None
        self.next = None

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, nextNode):
        self.next = nextNode

    def getNext(self):
        return self.next


class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, data, pos=None):
        newNode = Node()
        newNode.setData(data)
        if pos == 1:
            newNode.setNext(self.head)
            self.head = newNode
        elif pos is None and self.head is None:
            newNode.setNext(self.head)
            self.head = newNode
        elif pos is None and self.head is not None:
            current = self.head
            while current.next is not None:
                current = current.next
            current.setNext(newNode)
        else:
            current = self.head
            for i in range(1, pos - 1):
                current = current.next
            newNode.setNext(current.next)
            current.setNext(newNode)

    def delete(self, key=None, pos=None):
        prev = None
        current = self.head
        if pos is None or pos == 1:
            if (current.data == key and current.next is None) or (pos == 1 and current.next is None):
                self.head = None
                current.next = None
                return 'Node deleted'
            elif (current.data == key and current.next is not None) or (pos == 1 and current.next is not None):
                self.head = current.next
                current.next = None
                return 'Node deleted'
            else:
                current = self.head
                while current.data != key or current.next is not None:
                    prev = current
                    current = current.next
                if current.data == key:
                    prev.next = current.next
                    current.next = None
                    return 'Node deleted.'
                elif current.next is None:
                    return 'Key is not available in the Linked List.'
        else:
            for i in range(1, pos):
                prev = current
                current = current.next
            prev.next = current.next
            current.next = None
            return 'Node deleted.'

    def repr(self):
        if self.head is not None:
            current = self.head
            while current.next is not None:
                print(current.getData())
                current = current.next
            print(current.getData())
        else:
            print('Linked List is empty')

    def remove_loop(self):
        ID = list()
        prev = None
        current = self.head
        while id(current) not in ID:
            ID.append(id(current))
            prev = current
            current = current.next
        prev.next = None

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            Next = current.next
            current.next = prev
            prev = current
            current = Next
        self.head = prev
