
def quicksort(lst):
    """
    Quick Sort - nlog(n) avg, n^2 worst
    In memory sort
    swap middle with end
    two pointers move left, if found one > middle stop. move right and find stop
        swap
    """
    def quicksort(lst, left, right):
        middle = partition(lst, left, right)
        if left < middle-1:
            quicksort(lst, left, middle-1)
        if middle < right:
            quicksort(lst, middle, right)
    if len(lst) == 0:
        return lst
    quicksort(lst, 0, len(lst)-1)
    return lst

def partition(lst, left, right):
    middleValue = lst[(left + right)/2]
    while left <= right:
        while lst[left] < middleValue:
            left += 1
        while middleValue < lst[right]:
            right -= 1
        if left <= right:
            swap(lst, left, right)
            left += 1
            right -= 1
    return left

def swap(lst, pos1, pos2):
    temp = lst[pos1]
    lst[pos1] = lst[pos2]
    lst[pos2] = temp

##############################
import unittest

class Test(unittest.TestCase):

    def test_binarySearch_1(self):
        self.assertEqual([2,6,22,43,44,77], quicksort([6,43,22,77,44,2]))

    def test_binarySearch_2(self):
        self.assertEqual([4,6,9], quicksort([4,9,6]))

    def test_binarySearch_3(self):
        self.assertEqual([-8,-6,2,4,5], quicksort([-6,2,-8,4,5]))

    def test_binarySearch_4(self):
        self.assertEqual([1,5,8,10], quicksort([1,5,8,10]))

    def test_binarySearch_5(self):
        self.assertEqual([], quicksort([]))

if __name__ == '__main__':
    unittest.main()
