class Node(object):
    def __init__(self, key=None, data=None, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

class BST(object):
    """
    Binary Search Tree - O(log n)
    Property: Left child <= parent < right child
    Node requires a key.
    Good for storing numbered values in order.
    Inorder search should return a sorted key list
    """
    def __init__(self):
        self.root = None
        self.currentSize = 0

    def isBST(self):
        def isBST(root):
            if root is None:
                return True
            left = root.left
            right = root.right
            if left is not None and left.key > root.key:
                return False
            if right is not None and root.key >= right.key:
                return False
            else:
                return isBST(left) and isBST(right)

        return isBST(self.root)

    def search(self, key):
        def search(root, key):
            if root is None:
                return None
            if root.key == key:
                return root.data
            elif key < root.key:
                return search(root.left, key)
            elif root.key < key:
                return search(root.right, key)

        return search(self.root, key)

    def insert(self, key, data):
        def insert(root, newNode):
            if newNode.key <= root.key:
                if root.left is None:
                    root.left = newNode
                else:
                    insert(root.left, newNode)
            elif root.key < newNode.key:
                if root.right is None:
                    root.right = newNode
                else:
                    insert(root.right, newNode)

        newNode = Node(key, data)
        self.currentSize += 1
        if self.root is None:
            self.root = newNode
        else:
            insert(self.root, newNode)
        return self

    def remove(self, key):
        def findMinNode(root):
            current = root
            while current.left is not None:
                current = current.left
            return current

        def remove(root, key):
            if root is None:
                return None
            if key < root.key:
                root.left = remove(root.left, key)
            elif root.key < key:
                root.right = remove(root.right, key)
            elif root.key == key:
                if root.left is None and root.right is None:
                    return None
                elif root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                else:
                    minNode = findMinNode(root.right)
                    root.key = minNode.key
                    root.data = minNode.data
                    root.right = remove(root.right, minNode.key)
            return root
        return remove(self.root, key)


##############################
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        self.bst = BST()
        self.bst.insert(5, 5).insert(2, 2).insert(3, 3).insert(6, 6)

    def test_isBST(self):
        self.assertTrue(self.bst.isBST())

    def test_search_1(self):
        self.assertEqual(5, self.bst.search(5))
        self.assertEqual(6, self.bst.search(6))
        self.assertEqual(2, self.bst.search(2))
        self.assertEqual(3, self.bst.search(3))

    def test_search_2(self):
        self.assertEqual(None, self.bst.search(100))
        self.assertEqual(None, self.bst.search(None))

    def test_search_3(self):
        self.bst.insert(4, 4)
        self.assertEqual(4, self.bst.search(4))

    def test_insert_1(self):
        bst = BST()
        self.assertTrue(bst.isBST())

    def test_insert_2(self):
        bst = BST().insert(1,1).insert(2,2).insert(3,3).insert(4,4)
        self.assertTrue(bst.isBST())

    def test_insert_3(self):
        bst = BST().insert(5,5).insert(6,6).insert(7,7).insert(8,8).insert(1,1).insert(2,2).insert(3,3)
        self.assertTrue(bst.isBST())

    def test_remove_1(self):
        """
        Leaf Node Delete
        """
        self.bst.insert(7, 7)
        self.assertTrue(self.bst.isBST())
        self.assertEqual(7, self.bst.search(7))
        self.bst.remove(7)
        self.assertEqual(None, self.bst.search(7))
        self.assertTrue(self.bst.isBST())

    def test_remove_2(self):
        """
        Single Child Delete
        """
        self.assertTrue(self.bst.isBST())
        self.assertEqual(2, self.bst.search(2))
        self.bst.remove(2)
        self.assertEqual(None, self.bst.search(2))
        self.assertTrue(self.bst.isBST())

    def test_remove_3(self):
        """
        Double Child Delete Inner
        """
        self.bst.insert(1, 1)
        self.assertTrue(self.bst.isBST())
        self.assertEqual(2, self.bst.search(2))
        self.bst.remove(2)
        self.assertEqual(None, self.bst.search(2))
        self.assertTrue(self.bst.isBST())

    def test_remove_4(self):
        """
        Two Children Delete Root
        """
        self.assertTrue(self.bst.isBST())
        self.assertEqual(5, self.bst.search(5))
        self.bst.remove(5)
        self.assertEqual(None, self.bst.search(5))
        self.assertTrue(self.bst.isBST())

if __name__ == '__main__':
    unittest.main()
