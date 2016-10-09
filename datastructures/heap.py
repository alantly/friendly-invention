class Heap(object):
    """
    Min Binary Heap Implementation
    Property: Balanced and Complete
    """
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def getParentPosition(self, currentPosition):
        return currentPosition/2;

    def getChildPositionLeft(self, currentPosition):
        return currentPosition*2;

    def getChildPositionRight(self, currentPosition):
        return currentPosition*2 + 1;

    def printData(self):
        return "".join(map(str, self.heapList[1:self.currentSize+1]))

    def size(self):
        return self.currentSize

    def findMin(self):
        if self.currentSize > 0:
            return self.heapList[1]
        else:
            return None

    def insert(self, data):
        if data is None:
            return self
        self.currentSize += 1
        if len(self.heapList) > self.currentSize:
            self.heapList[self.currentSize] = data
        else :
            self.heapList.append(data)
        self.swiftup(self.currentSize)
        return self

    def swiftup(self, currentPosition):
        if currentPosition == 0:
            return
        parentPos = self.getParentPosition(currentPosition)
        parent = self.heapList[parentPos]
        me = self.heapList[currentPosition]
        if parent > me:
            self.swap(parentPos, currentPosition)
        self.swiftup(parentPos)

    def swap(self, pos1, pos2):
        temp = self.heapList[pos1]
        self.heapList[pos1] = self.heapList[pos2]
        self.heapList[pos2] = temp

    def removeMin(self):
        top = self.findMin()
        if top is not None:
            lastItem = self.heapList[self.currentSize]
            self.heapList[1] = lastItem
            self.currentSize -= 1
            self.swiftDown(1)
        return top

    def swiftDown(self, currentPosition):
        top = self.heapList[currentPosition]
        leftChild = self.getChildPositionLeft(currentPosition)
        rightChild = self.getChildPositionRight(currentPosition)
        if leftChild <= self.currentSize and top > self.heapList[leftChild]:
            self.swap(currentPosition, leftChild)
            self.swiftDown(leftChild)
        elif rightChild <= self.currentSize and top > self.heapList[rightChild]:
            self.swap(currentPosition, rightChild)
            self.swiftDown(rightChild)

##############################
import unittest

class TestLinkLists(unittest.TestCase):

    def setUp(self):
        self.heap = Heap()
        self.heap.insert(6).insert(9).insert(2).insert(4)

    def test_printData(self):
        self.assertEqual("2469", self.heap.printData())

    def test_size(self):
        self.assertEqual(4, self.heap.size())

    def test_findMin_1(self):
        self.assertEqual(None, Heap().findMin())

    def test_findMin_2(self):
        self.assertEqual(2, self.heap.findMin())

    def test_insert_1(self):
        self.assertEqual("2469", self.heap.printData())
        self.heap.insert(5)
        self.assertEqual("24695", self.heap.printData())
        self.heap.insert(1)
        self.assertEqual("142956", self.heap.printData())
        self.heap.insert(10)
        self.assertEqual("14295610", self.heap.printData())

    def test_insert_2(self):
        self.assertEqual("2469", self.heap.printData())
        self.heap.insert(None)
        self.assertEqual("2469", self.heap.printData())

    def test_removeMin_1(self):
        self.assertEqual("2469", self.heap.printData())
        self.heap.removeMin()
        self.assertEqual("496", self.heap.printData())

    def test_removeMin_2(self):
        self.assertEqual("2469", self.heap.printData())
        self.assertEqual(2, self.heap.removeMin())
        self.assertEqual(4, self.heap.removeMin())
        self.assertEqual(6, self.heap.removeMin())
        self.assertEqual(9, self.heap.removeMin())
        self.assertEqual(None, self.heap.removeMin())
        self.assertEqual("", self.heap.printData())

    def test_insert_removeMin(self):
        heap = Heap()
        heap.insert(5)
        self.assertEqual(5, heap.removeMin())
        heap.insert(6).insert(2).insert(1)
        self.assertEqual("162", heap.printData())

if __name__ == '__main__':
    unittest.main()