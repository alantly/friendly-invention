Tools
Link List/Array - general list of values - O(n)
Stack - useful for keeping the most recent item - O(n)
Queue - useful for keeping a line of items/oldest item - O(n)
Heap - useful for min/max removes - O(log n)
Binary Search Tree - good for storing numbered values in order - O(log n)
Hash Table/Hash Set - good for constant access and unique values - O(1)
Recursion - idea is to keep and edit original state as function input and return result at bottom. (Good for string manip and Binary Trees)

5 Algorithm Approaches
Examplify - build small examples to see problem
Pattern Matching - find similar problems and alter solution
Simplify and Generalize - find a solution for a simplier problem
Base Case and Build - Recursion
Data Structure Brainstorm - run through a list of data structures for best fits

Algorithms
For lists of values
  Binary Search - O(log n)
  Quick Sort - O(n log n)
  Merge Sort - O(n log n)
Binary Trees
  Preorder - O(|V|)
  Inorder - O(|V|)
  Postorder - O(|V|)
For Graphs
  DFS - Recursive/Iterative O(|V| + |E|)
  BFS  - Iterative O(|V| + |E|)

Data Structures
Linked List
-check for null and update accordingly
-slow faster runner technique
-theta(n) to march down list
-doubly linked list contains prev and next

index T(n)
insert/delete at beg T(1)
insert/delete at end T(n) or T(1)
insert/delete at middle T(1) + search time
Wasted space average T(n)

Binary Tree
-Binary Tree (tree of 2 elements) vs. Binary Search Tree (left <= root < right)
class Tree {
  int entry;
  Node left_child = null;
  Node right_child = null;
  public Tree(int e, Node l = null, Node r = null) {
    entry = e;
    left_child = l;
    right_child = r;
  }
}
-Recursion based traversal, dont think about dfs or bfs, like in 61a. just pre,in, and post
-balanced vs unbalanced (describe in avg and worst case)
-Full (every node has k children) and Complete (all children at the kth or k-1th level). Both is rare with (2^n) -1 nodes
-red-black
-avl

-Pre-order traversal = visit every node BEFORE its children (regular left to right dfs traversal)
void preorder(Node root) {
  if (root == NULL) return;
  visit(root);
  preorder(root->left());
  preorder(root->right());
}
-in-order = visit left leaf then node then right leaf. goes to the bottom first.
go left
visit root
go right
-post-order = visit node AFTER its children (used to delete children then node)
go left
go right
visit root
-Tree Balancing: Need runtime and idea of how they work
Red-Black Tree - O(log n)
AVL Trees - O(log n)

Tries
-n-ary tree using chars as nodes. builds words in traversal. prefix tree??

Graphs
-Build using hash table and adjanency list.
-Keep searched nodes using hashset
-Traverse using BFS/DFS
-Dijkstra's for distances, shortest path
-Prims algorithm, min spanning tree

Vectors/ArrayLists
-dynamically resizing array provide O(1) access time
-double size when hit limit, O(n) time

Hash Table
-always use this as a set
-fast lookup in an array, hash function maps key to array index
-keys need to be unique, large table.
-can use BST for O(logn) lookup or linklist for O(n)
Space   O(n)   O(n)
Search   O(1)   O(n)
Insert   O(1)   O(n)
Delete   O(1)   O(n)

Algorithms
Breath First Search - O(|V| + |E|)
Iterative
void search(Node root) {
  Queue queue = new Queue();
  root.visited = true;
  visit(root);
  queue.enqueue(root); // Add to end of queue
  while (!queue.isEmpty()) {
    Node r = queue.dequeue(); // Remove from front of queue
    visit(r);
    r.visited = true;
    foreach (Node n in r.adjacent) {
      if (n.visited == false) {
        queue.enqueue(n);
      }
    }
  }
}
Depth First Search - O(|V| + |E|)
Recursive
void search(Node root) {
if (root == null) return;
  visit(root);
  root.visited = true;
  foreach (Node n in root.adjacent) {
    if (n.visited == false) {
      search(n);
    }
  }
}

Binary Search - O(log n)
int binarySearch(int[] a, int x) {
  int low = 0;
  int high = a.length - 1;
  int mid;
  while (low <= high) {
    mid = (low + high) / 2;
    if (a[mid] < x) {
      low = mid + 1;
    } else if (a[mid] > x) {
      high = mid - 1;
    } else {
      return mid;
    }
  }
  return -1; // Error
}

int binarySearchRecursive(int[] a, int x, int low, int high) {
  if (low > high) return -1; // Error

  int mid = (low + high) / 2;
  if (a[mid] < x) {
    return binarySearchRecursive(a, x, mid + 1, high);
  } else if (a[mid] > x) {
    return binarySearchRecursive(a, x, low, mid - 1);
  } else {
    return mid;
  }
}


Merge Sort - nlog(n) in avg and worst, memory depends, good for linklists
void mergesort(int[] array) {
  int[] helper = new int[array.length];
  mergesort(array, helper, 0, array.length - 1);
}

void mergesort(int[] array, int[] helper, int low, int high) {
  if (low < high) {
    int middle = (low + high) / 2;
    mergesort(array, helper, low, middle); // Sort left half
    mergesort(array, helper, middle+1, high); // Sort right half
    merge(array, helper, low, middle, high); // Merge them
  }
}

void merge(int[] array, int[] helper, int low, int middle, int high) {
  /* Copy both halves into a helper array */
  for (int i = low; i <= high; i++) {
    helper[i] = array[i];
  }

  int helperLeft = low;
  int helperRight = middle + 1;
  int current = low;

  /* Iterate through helper array. Compare the left and right
  * half, copying back the smaller element from the two halves
  * into the original array. */
  while (helperLeft <= middle && helperRight <= high) {
    if (helper[helperLeft] <= helper[helperRight]) {
      array[current] = helper[helperLeft];
      helperLeft++;
    } else { // If right element is smaller than left element
      array[current] = helper[helperRight];
      helperRight++;
    }
    current++;
  }

  /* Copy the rest of the left side of the array into the
  * target array */
  int remaining = middle - helperLeft;
  for (int i = 0; i <= remaining; i++) {
    array [current + i] = helper[helperLeft + i]j
  }
}


Quick Sort - nlog(n) avg, n^2 worst, memory in log(n)
void quickSort(int arr[], int left, int right) {
  int index = partition(arr, left, right);
  if (left < index - 1 ) { / / Sort left half
    quickSort(arr, left, index - 1);
  }
  if (index < right) { // Sort right half
    quickSort(arr, index, right);
  }
}

int partition(int arr[], int left, int right) {
  int pivot = arr[(left + right) / 2]; // Pick pivot point
  while (left <= right) {

    // Find element on left that should be on right
    while (arr[left] < pivot) left++;

    // Find element on right that should be on left
    while (arr[right] > pivot) right--;

    // Swap elements, and move left and right indices
    if (left <= right) {
      swap(arr, left, right); // swaps elements
      left++;
      right--;
    }
  }
  return left;
}

Concepts
Bit Manipulation
- << shifts/mul by 2, >> div by 2, ^ XOR, & and, ~negate, | or

OOP
-ask questions, who what when where why and how?
-define core objects
-what is relationship, inheritances? one to many or many to many
-investigate patterns
Singleton Design Pattern - single global object with exactly one instance
Factory Design Pattern - interface to create multiple instances
polymorphism - single interface to multiple implementations
inheritance
Dynamic binding -> Human h = new Boy()
Static Binding -> Boy b = new Boy()

Scalability
1.Solve in perfect world
2.Get real (limitations in data,etc)
3.Solve with complications
Remember HDD space, RAM, and Internet transfer latency
Divide data - add space when needed, hash and mod hash, similar values, simple look up table

C, C++ Specifics
Private by default
Virtual Functions - useful for freeing memory
static-binding (calls parent if not virtual)
override - inheritace
overload - operator overload

Java Specifics
final - diff in variable, method, and class
Static - Overloading is method with same name but different arguments
Dynamic - Overriding is method with same name and signature, but different than super class
Interface - virtual class

Threads and Locks

Memory(Stack vs. Heap)
Recursion
Big-O Time

Big endian - Store most significant byte in smallest address (read left to right in memory)
little endian - store leaste significant byte in smallest address (read from right to left)
