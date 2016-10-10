5 Algorithm Approaches
Examplify - build small examples to see problem
Pattern Matching - find similar problems and alter solution
Simplify and Generalize - find a solution for a simplier problem
Base Case and Build - Recursion
Data Structure Brainstorm - run through a list of data structures for best fits

Algorithms
For lists of values
  Quick Sort - O(n log n)
  Merge Sort - O(n log n)
For Graphs
  DFS - Recursive/Iterative O(|V| + |E|)
  BFS  - Iterative O(|V| + |E|)

Binary Tree
-red-black
-avl

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
-loop in graph

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
