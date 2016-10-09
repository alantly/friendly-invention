class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def printData(head):
    if head is None:
        return ""
    return head.data + printData(head.next)

def size(head):
    if head is None:
        return 0
    return 1 + size(head.next)

def findNode(head, data):
    if head is None:
        return
    if head.data == data:
        return head
    else:
        return findNode(head.next, data)

def append(head, node):
    if head is None:
        return node
    current = head
    while current.next is not None:
        current = current.next
    current.next = node
    return head

def delete(head, data):
    if head is None:
        return None
    if head.data == data:
        return head.next
    prev = head
    current = head.next
    while current is not None:
        if current.data == data:
            prev.next = current.next
            return head
        prev = current
        current = current.next
    return head

##############################
import unittest

class TestLinkLists(unittest.TestCase):

    def setUp(self):
        self.end = Node("!")
        self.middle = Node("world ", self.end)
        self.top = Node("hello ", self.middle)

    def test_printData(self):
        self.assertEqual("hello world !", printData(self.top))

    def test_size(self):
        self.assertEqual(3, size(self.top))

    def test_findNode(self):
        self.assertEqual(self.top.next.next, findNode(self.top, "!"))
        self.assertEqual(self.top, findNode(self.top, "hello "))
        self.assertEqual(None, findNode(self.top, "invalid"))

    def test_append_1(self):
        sample = Node("test data")
        self.assertEqual(sample, append(None, sample))

    def test_append_2(self):
        self.assertEqual("hello world !", printData(self.top))
        append(self.top, Node(" Again", Node(" World")))
        self.assertEqual("hello world ! Again World", printData(self.top))

    def test_delete_1(self):
        self.assertEqual("hello world !", printData(self.top))
        delete(self.top, self.end.data)
        self.assertEqual("hello world ", printData(self.top))

    def test_delete_2(self):
        self.assertEqual("hello world !", printData(self.top))
        delete(self.top, self.middle.data)
        self.assertEqual("hello !", printData(self.top))

    def test_delete_3(self):
        self.assertEqual("hello world !", printData(self.top))
        delete(self.top, None)
        delete(self.top, "some random data")
        self.assertEqual("hello world !", printData(self.top))

if __name__ == '__main__':
    unittest.main()
