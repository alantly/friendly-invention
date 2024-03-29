from node import Node

class Queue(object):
    """
    Queue O(n)
    Property: FIFO (First in First out)
    Useful for keeping a line of items/oldest item
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.currentSize = 0

    def printData(self):
        if self.head is None:
            return ""
        return self.head.printData()

    def size(self):
        return self.currentSize

    def peek(self):
        if self.head is None:
            return None
        return self.head.data

    def enqueue(self, data):
        if data is None:
            return self
        self.currentSize += 1
        newTail = Node(data)
        if self.head is None:
            self.head = self.tail = newTail
        else:
            self.tail.next = newTail
            self.tail = newTail
        return self

    def dequeue(self):
        if self.head is None:
            return None
        self.currentSize -= 1
        dequeuedNode = self.head
        self.head = self.head.next
        return dequeuedNode.data

##############################
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()
        self.queue.enqueue("1").enqueue("2").enqueue("3").enqueue("4")

    def test_printData(self):
        self.assertEqual("1234", self.queue.printData())

    def test_size(self):
        self.assertEqual(4, self.queue.size())

    def test_peek_1(self):
        self.assertEqual(None, Queue().peek())

    def test_peek_2(self):
        self.assertEqual("1", self.queue.peek())

    def test_enqueue_1(self):
        self.assertEqual("1234", self.queue.printData())
        self.queue.enqueue("5")
        self.assertEqual("12345", self.queue.printData())

    def test_enqueue_2(self):
        self.assertEqual("1234", self.queue.printData())
        self.queue.enqueue(None)
        self.assertEqual("1234", self.queue.printData())

    def test_dequeue_1(self):
        self.assertEqual("1234", self.queue.printData())
        self.queue.dequeue()
        self.assertEqual("234", self.queue.printData())

    def test_dequeue_2(self):
        self.assertEqual("1234", self.queue.printData())
        self.assertEqual("1", self.queue.dequeue())
        self.assertEqual("2", self.queue.dequeue())
        self.assertEqual("3", self.queue.dequeue())
        self.assertEqual("4", self.queue.dequeue())
        self.assertEqual(None, self.queue.dequeue())
        self.assertEqual("", self.queue.printData())

    def test_enqueue_dequeue(self):
        queue = Queue()
        queue.enqueue("1")
        self.assertEqual("1", queue.dequeue())
        queue.enqueue("2").enqueue("4")
        self.assertEqual("24", queue.printData())

if __name__ == '__main__':
    unittest.main()
