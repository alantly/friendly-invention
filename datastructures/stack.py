class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def printData(self):
        if self.next is None:
            return self.data
        return self.data + self.next.printData()

    def size(self):
        if self.next is None:
            return 1
        return 1 + self.next.size()

class Stack(object):
    def __init__(self):
        self.head = None

    def printData(self):
        if self.head is None:
            return ""
        return self.head.printData()

    def size(self):
        if self.head is None:
            return 0
        return self.head.size()

    def peek(self):
        if self.head is None:
            return None
        return self.head.data

    def push(self, data):
        if data is None:
            return self
        newHead = Node(data)
        newHead.next = self.head
        self.head = newHead
        return self

    def pop(self):
        if self.head is None:
            return None
        poppedData = self.head
        self.head = self.head.next
        return poppedData.data


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

    def test_push_1(self):
        self.assertEqual("4321", self.stack.printData())
        self.stack.push("9")
        self.assertEqual("94321", self.stack.printData())

    def test_push_2(self):
        self.assertEqual("4321", self.stack.printData())
        self.stack.push(None)
        self.assertEqual("4321", self.stack.printData())

    def test_peek_1(self):
        self.assertEqual(None, Stack().peek())

    def test_peek_2(self):
        self.assertEqual("4", self.stack.peek())

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

if __name__ == '__main__':
    unittest.main()
