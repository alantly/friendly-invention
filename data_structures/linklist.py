from node import Node

class LinkList(object):
    """
    Link List/Array - O(n)
    General list of values
    - Check for null and update accordingly
    - Slow faster runner technique
    - theta(n) to march down list
    - doubly linked list contains prev and next

    Vectors/ArrayLists
    - dynamically resizing array provide O(1) access time
    - double size when hit limit - O(n) time
    """
    def __init__(self):
        self.head = None
        self.currentSize = 0

    def printData(self):
        if self.head is None:
            return ""
        return self.head.printData()

    def size(self):
        return self.currentSize

    def invalidPosition(self, position):
        return position is None or position >= self.size() or position < 0

    def get(self, position):
        if self.head is None or self.invalidPosition(position):
            return None
        current = self.head
        for i in range(position):
            current = current.next
        return current.data

    def append(self, data):
        if data is None:
            return None
        self.currentSize += 1
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode
        return self

    def insert(self, position, data):
        if data is None:
            return None
        if self.invalidPosition(position):
            return self.append(data)
        else:
            self.currentSize += 1
            newNode = Node(data)
            if position == 0:
                newNode.next = self.head
                self.head = newNode
            else:
                current = self.head
                for i in range(position):
                    current = current.next
                newNode.next = current.next
                current.next = newNode
        return self

    def delete(self, position):
        if self.head is None or self.invalidPosition(position):
            return None
        self.currentSize -= 1
        if position == 0:
            deletedData = self.head.data
            self.head = self.head.next
        else:
            prev = self.head
            current = self.head.next
            for i in range(position-1):
                prev = current
                current = current.next
            deletedData = current.data
            prev.next = current.next
        return deletedData

##############################
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        self.linklist = LinkList()
        self.linklist.append("1").append("2").append("3").append("4")

    def test_printData(self):
        self.assertEqual("1234", self.linklist.printData())

    def test_size(self):
        self.assertEqual(4, self.linklist.size())

    def test_get_1(self):
        self.assertEqual(None, LinkList().get(0))

    def test_get_2(self):
        self.assertEqual(None, self.linklist.get(None))
        self.assertEqual(None, self.linklist.get(-1))
        self.assertEqual("1", self.linklist.get(0))
        self.assertEqual("3", self.linklist.get(2))
        self.assertEqual("4", self.linklist.get(3))
        self.assertEqual(None, self.linklist.get(7))

    def test_append_1(self):
        self.assertEqual("1234", self.linklist.printData())
        self.linklist.append("9")
        self.assertEqual("12349", self.linklist.printData())

    def test_append_2(self):
        self.assertEqual("1234", self.linklist.printData())
        self.linklist.append(None)
        self.assertEqual("1234", self.linklist.printData())

    def test_insert_1(self):
        self.assertEqual("1234", self.linklist.printData())
        self.linklist.insert(0, "9")
        self.assertEqual("91234", self.linklist.printData())
        self.linklist.insert(2, "5")
        self.assertEqual("912534", self.linklist.printData())
        self.linklist.insert(6, "7")
        self.assertEqual("9125347", self.linklist.printData())

    def test_insert_2(self):
        self.assertEqual("1234", self.linklist.printData())
        self.linklist.insert(None, "5")
        self.assertEqual("12345", self.linklist.printData())
        self.linklist.insert(2, None)
        self.assertEqual("12345", self.linklist.printData())

    def test_delete_1(self):
        self.assertEqual("1234", self.linklist.printData())
        self.linklist.delete(0)
        self.assertEqual("234", self.linklist.printData())
        self.linklist.delete(1)
        self.assertEqual("24", self.linklist.printData())

    def test_delete_2(self):
        self.assertEqual("1234", self.linklist.printData())
        self.assertEqual("1", self.linklist.delete(0))
        self.assertEqual("2", self.linklist.delete(0))
        self.assertEqual("3", self.linklist.delete(0))
        self.assertEqual("4", self.linklist.delete(0))
        self.assertEqual(None, self.linklist.delete(0))
        self.assertEqual("", self.linklist.printData())

    def test_append_delete(self):
        linklist = LinkList()
        linklist.append("1")
        self.assertEqual("1", linklist.delete(0))
        linklist.append("6").append("2")
        self.assertEqual("62", linklist.printData())

if __name__ == '__main__':
    unittest.main()
