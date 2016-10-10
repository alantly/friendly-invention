from Queue import Queue

class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

def balanced(root):
    """
    Depth between leaf nodes is at most a difference of 1
    """
    if root is None:
        return True
    if abs(height(root.left) - height(root.right)) > 1:
        return False
    else:
        return balanced(root.left) and balanced(root.right)

def complete(root):
    """
    All children at the kth or k-1th level
    """
    pass

def full(root):
    """
    Every node has k children
    """
    pass

def bfs(root):
    """
    breath first search
    """
    if root is None:
        return
    result = []
    queue = Queue()
    queue.put(root)
    while not queue.empty():
        current = queue.get()
        result.append(current.data)
        if current.left is not None:
            queue.put(current.left)
        if current.right is not None:
            queue.put(current.right)
    return result

def dfs_preorder(root):
    """
    Preorder - O(|V|)
    Property: Visit parent first before children. Standard DFS.
    """
    if root is None:
        return []
    return [root.data] + dfs_preorder(root.left) + dfs_preorder(root.right)

def dfs_inorder(root):
    """
    Inorder - O(|V|)
    Property: Visit left. Middle. Right. Goes to the left most bottom first.
    """
    if root is None:
        return []
    return dfs_inorder(root.left) + [root.data] + dfs_inorder(root.right)

def dfs_postorder(root):
    """
    Postorder - O(|V|)
    Property: Go to children first. Visit parent last.
    Good for entire tree deletion
    """
    if root is None:
        return []
    return dfs_postorder(root.left) + dfs_postorder(root.right) + [root.data]

##############################
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        """
             1
          6      3
            5  2   4
                  7
        """
        self.root = Node(1, Node(6, None, Node(5)), Node(3, Node(2), Node(4, Node(7))))

    def test_height(self):
        self.assertEquals(0, height(None))
        self.assertEquals(4, height(self.root))
        self.assertEquals(2, height(Node(6, None, Node(5))))

    def test_balanced(self):
        balancedTree = Node(1, Node(6, None, Node(5)), Node(3, Node(2), Node(4, Node(7))))
        self.assertTrue(balanced(balancedTree))
        inbalancedTree = Node(1, Node(6, None, Node(5)), Node(3, Node(2), Node(4, Node(7, Node(9)))))
        self.assertFalse(balanced(inbalancedTree))

    def test_bfs(self):
        self.assertEqual([1,6,3,5,2,4,7], bfs(self.root))

    def test_dfs_preorder(self):
        self.assertEqual([1,6,5,3,2,4,7], dfs_preorder(self.root))

    def test_dfs_inorder(self):
        self.assertEqual([6,5,1,2,3,7,4], dfs_inorder(self.root))

    def test_dfs_postorder(self):
        self.assertEqual([5,6,2,7,4,3,1], dfs_postorder(self.root))

if __name__ == '__main__':
    unittest.main()
