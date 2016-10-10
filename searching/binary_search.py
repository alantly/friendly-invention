
def binarySearchRec(lst, key):
    """
    Search in O(log n)
    """
    def binarySearch(lst, left, right, key):
        if left > right:
            return None
        middle = (left + right)/2
        if lst[middle] == key:
            return middle
        elif lst[middle] < key:
            return binarySearch(lst, middle+1, right, key)
        else:
            return binarySearch(lst, left, middle-1, key)
    return binarySearch(lst, 0, len(lst)-1, key)

def binarySearchIter(lst, key):
    """
    Search in O(log n)
    """
    left = 0
    right = len(lst)-1
    while left <= right:
        middle = (left + right)/2
        if lst[middle] == key:
            return middle
        elif lst[middle] < key:
            left = middle+1
        else:
            right = middle-1
    return None

##############################
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        self.list = [2,3,5,7,9,22,42,44,64]

    def test_binarySearch_1(self):
        self.assertEqual(3, binarySearchRec(self.list, 7))
        self.assertEqual(3, binarySearchIter(self.list, 7))

    def test_binarySearch_2(self):
        self.assertEqual(0, binarySearchRec(self.list, 2))
        self.assertEqual(0, binarySearchIter(self.list, 2))

    def test_binarySearch_3(self):
        self.assertEqual(8, binarySearchRec(self.list, 64))
        self.assertEqual(8, binarySearchIter(self.list, 64))

    def test_binarySearch_4(self):
        self.assertEqual(None, binarySearchRec(self.list, 15))
        self.assertEqual(None, binarySearchIter(self.list, 15))

if __name__ == '__main__':
    unittest.main()
