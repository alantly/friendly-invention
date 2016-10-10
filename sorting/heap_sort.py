from Queue import PriorityQueue

def heapsort(lst):
    """
    Heap Sort - nlog(n)
    """
    result = []
    heap = PriorityQueue()
    for i in lst:
        heap.put(i)
    while not heap.empty():
        result.append(heap.get())
    return result

##############################
import unittest

class Test(unittest.TestCase):

    def test_binarySearch_1(self):
        self.assertEqual([2,6,22,43,44,77], heapsort([6,43,22,77,44,2]))

    def test_binarySearch_2(self):
        self.assertEqual([4,6,9], heapsort([4,9,6]))

    def test_binarySearch_3(self):
        self.assertEqual([-8,-6,2,4,5], heapsort([-6,2,-8,4,5]))

    def test_binarySearch_4(self):
        self.assertEqual([1,5,8,10], heapsort([1,5,8,10]))

    def test_binarySearch_5(self):
        self.assertEqual([], heapsort([]))

if __name__ == '__main__':
    unittest.main()
