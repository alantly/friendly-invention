class Heap(object):
    """
    Min Binary Heap - O(log n)
    Property: Balanced and Complete Binary Tree
    Useful for min/max removes. Also know as priority queue. Can be used for heapsort.
    """
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def checkMinProperty(self):
        for i in range(1, self.currentSize+1):
            leftChild = self.getChildPositionLeft(i)
            rightChild = self.getChildPositionRight(i)
            if leftChild <= self.currentSize and self.heapList[i] > self.heapList[leftChild]:
                return False
            elif rightChild <= self.currentSize and self.heapList[i] > self.heapList[rightChild]:
                return False
        return True

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
        minChild = self.getMinChild(currentPosition)
        if minChild != -1 and top > self.heapList[minChild]:
            self.swap(currentPosition, minChild)
            self.swiftDown(minChild)

    def getMinChild(self, currentPosition):
        leftChild = self.getChildPositionLeft(currentPosition)
        rightChild = self.getChildPositionRight(currentPosition)
        if rightChild <= self.currentSize:
            if self.heapList[leftChild] < self.heapList[rightChild]:
                return leftChild
            else:
                return rightChild
        elif leftChild <= self.currentSize:
            return leftChild
        else:
            return -1

##############################
import unittest

class TestLinkLists(unittest.TestCase):

    def setUp(self):
        self.heap = Heap()
        self.heap.insert(6).insert(9).insert(2).insert(4)
        self.assertTrue(self.heap.checkMinProperty())

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
        self.assertTrue(self.heap.checkMinProperty())

    def test_insert_2(self):
        self.assertEqual("2469", self.heap.printData())
        self.heap.insert(None)
        self.assertEqual("2469", self.heap.printData())
        self.assertTrue(self.heap.checkMinProperty())

    def test_removeMin_1(self):
        self.assertEqual("2469", self.heap.printData())
        self.heap.removeMin()
        self.assertEqual("496", self.heap.printData())
        self.assertTrue(self.heap.checkMinProperty())

    def test_removeMin_2(self):
        self.assertEqual("2469", self.heap.printData())
        self.assertEqual(2, self.heap.removeMin())
        self.assertEqual(4, self.heap.removeMin())
        self.assertEqual(6, self.heap.removeMin())
        self.assertEqual(9, self.heap.removeMin())
        self.assertEqual(None, self.heap.removeMin())
        self.assertEqual("", self.heap.printData())
        self.assertTrue(self.heap.checkMinProperty())

    def test_removeMin_3(self):
        heap = Heap()
        heap.insert(1).insert(3).insert(2).insert(7)
        self.assertEqual("1327", heap.printData())
        self.assertEqual(1, heap.removeMin())
        self.assertEqual("237", heap.printData())
        self.assertTrue(heap.checkMinProperty())

    def test_insert_removeMin(self):
        heap = Heap()
        heap.insert(5)
        self.assertEqual(5, heap.removeMin())
        heap.insert(6).insert(2).insert(1)
        self.assertEqual("162", heap.printData())
        self.assertTrue(heap.checkMinProperty())

if __name__ == '__main__':
    unittest.main()
