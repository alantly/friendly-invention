class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def printData(self):
        if self.next is None:
            return self.data
        return self.data + self.next.printData()
