
def mergesort(lst):
    """
    Merge Sort - nlog(n) in avg and worst
    Good for linklists
    Good for large files. Unix sort
    """
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return lst
    middle = len(lst)/2
    return merge(mergesort(lst[:middle]), mergesort(lst[middle:]))

def merge(lst1, lst2):
    lst1Pos = 0
    lst2Pos = 0
    result = []
    while lst1Pos < len(lst1) and lst2Pos < len(lst2):
        if lst1[lst1Pos] <= lst2[lst2Pos]:
            result.append(lst1[lst1Pos])
            lst1Pos+=1
        elif lst1[lst1Pos] > lst2[lst2Pos]:
            result.append(lst2[lst2Pos])
            lst2Pos+=1
    if lst1Pos < len(lst1):
        result = result + lst1[lst1Pos:]
    else:
        result = result + lst2[lst2Pos:]
    return result

##############################
import unittest

class Test(unittest.TestCase):

    def test_binarySearch_1(self):
        self.assertEqual([2,6,22,43,44,77], mergesort([6,43,22,77,44,2]))

    def test_binarySearch_2(self):
        self.assertEqual([4,6,9], mergesort([4,9,6]))

    def test_binarySearch_3(self):
        self.assertEqual([-8,-6,2,4,5], mergesort([-6,2,-8,4,5]))

    def test_binarySearch_4(self):
        self.assertEqual([1,5,8,10], mergesort([1,5,8,10]))

    def test_binarySearch_5(self):
        self.assertEqual([], mergesort([]))

if __name__ == '__main__':
    unittest.main()
