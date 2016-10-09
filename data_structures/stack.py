class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def printData(self):
        if self.next is None:
            return self.data
        return self.data + self.next.printData()

class Stack(object):
    def __init__(self):
        self.head = None
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

    def push(self, data):
        if data is None:
            return self
        self.currentSize += 1
        newHead = Node(data)
        newHead.next = self.head
        self.head = newHead
        return self

    def pop(self):
        if self.head is None:
            return None
        self.currentSize -= 1
        poppedNode = self.head
        self.head = self.head.next
        return poppedNode.data

##############################
import unittest

class TestLinkLists(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()
        self.stack.push("1").push("2").push("3").push("4")

    def test_printData(self):
        self.assertEqual("4321", self.stack.printData())

    def test_size(self):
        self.assertEqual(4, self.stack.size())

    def test_peek_1(self):
        self.assertEqual(None, Stack().peek())

    def test_peek_2(self):
        self.assertEqual("4", self.stack.peek())

    def test_push_1(self):
        self.assertEqual("4321", self.stack.printData())
        self.stack.push("9")
        self.assertEqual("94321", self.stack.printData())

    def test_push_2(self):
        self.assertEqual("4321", self.stack.printData())
        self.stack.push(None)
        self.assertEqual("4321", self.stack.printData())

    def test_pop_1(self):
        self.assertEqual("4321", self.stack.printData())
        self.stack.pop()
        self.assertEqual("321", self.stack.printData())

    def test_pop_2(self):
        self.assertEqual("4321", self.stack.printData())
        self.assertEqual("4", self.stack.pop())
        self.assertEqual("3", self.stack.pop())
        self.assertEqual("2", self.stack.pop())
        self.assertEqual("1", self.stack.pop())
        self.assertEqual(None, self.stack.pop())
        self.assertEqual("", self.stack.printData())

    def test_push_pop(self):
        stack = Stack()
        stack.push("1")
        self.assertEqual("1", stack.pop())
        stack.push("6").push("2")
        self.assertEqual("26", stack.printData())

if __name__ == '__main__':
    unittest.main()
