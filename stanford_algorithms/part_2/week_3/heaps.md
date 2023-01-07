### Data Structures

- Point:
    - Organize data so that it can be accessed quickly and usefully.

- Examples:
    - lists, stacks, queues, heaps, search trees, hash tables, bloom filters,
      union-find, etc.

- Why so many?
    - Different data structures support different sets of operations.
      -> Suitable for different types of tasks

- Rule of Thumb:
    - Choose the "minimal" data structure that supports all the operations you
      need, but no superfluous ones.

Level 0 - "What's a data structure?"
Level 1 - cocktail party-level literacy
Level 2 - "this problem calls for a heap"
Level 3 - "I only use data structures that I wrote myself"

### Heap: Operations and Applications

- A container for objects that have keys
    - Key/Value -> SIN #/Employee records, Weight of Edge/Network Edges, Time to
      Occur/Event

- Supported Operations:
    - INSERT: add a new object to the heap.
        - Running Time: O(log n)
    - EXTRACT-MIN or EXTRACT-MAX: Remove an object in heap with a
      minimum/maximum key value.
        - Running Time: O(log n)
    - HEAPIFY: (n batched inserts in O(n) time)
    - DELETE: (O(log n) time)

- Canonical Use Of Heap:
    - Fast way to do repeated minimum computations.

- Example:
    - SelectionSort O(n^2) -> HeapSort
        - Insert all n array elements into a heap
        - Extract-Min to pluck out the elements in sorted order
        - Running Time: 2n heap operations = O(n log n) time
            - Optimal for a "comparison-based" sorting algorithm!

    - Event Manager / "Priority Queue"
        - Priority Queue is synonym for heap
        - Example: Simulation (e.g., for a video game)
        - objects = event
          records [action/update to occur at a given time in the future]
        - key = time event scheduled to occur
        - Extract-Min => yields the next scheduled event

    - Median Maintenance
        - I give you: a sequence x_1, ..., x_n of numbers, one-by-one.
        - You tell me: at each time step i, the median of { x_1, ..., x_i }.
        - Constraint: use O(log i)
        - Solution:
            - Maintain heaps H_low (w/ extract-max) and H_high (w/ extract-min)
        - Key idea:
            - Maintain invariant that ~= i/2 smallest (largest) elements in
              H_low (H_high)
            - If new number is less than max of H_low, add to H_low
            - If new number is greater than min of H_high, add to H_high
            - If there is imbalance b/w H_low and H_high, extract and insert
              into other heap
            - Median:
                - If i is even, either max of H_low and min of H_high
                - If i is odd, extract element from heap with additional element

    - Speeding up Dijkstra's Shortest Path Algorithm:
        - Naive implementation => runtime = O(n * m)
            - n = # of loop iterations
            - m = work per iteration (linear scan through edges for minimum
              computation)
            - with heaps => run time = O(m log n)

### Heap Implementation

- Conceptually: Think of a heap as a tree.
    - Rooted, balanced binary tree, as complete as possible
- Heap property: at every node x,
    - key[x] <= all of x's children

- Array Implementation:
    - parent(i) -> {even: i / 2, odd: floor(i / 2)}
    - children(i) -> 2 * i, 2 * i + 1
    - Insertion: 
        - Given key k, append to end of last level
        - If key k is less than its parent:
            - Swap with parent recursively, until parent is <= than key k
              (Bubble up)
    - Extract Min: 
        - Rip off the Root
        - Move last leaf to be the new root
        - Swap new root with smaller child recursively until it has no 
          children (Bubble down)

### Balanced Search Trees

- What is it good for?
    - Dynamic version of a sorted array.

- Sorted Array Operations:
    - Search (Binary Search) -> O(log n)
    - Selection (given order statistic i) -> O(1)
    - Min / Max -> O(1)
    - Predecessor / Successor (given pointer to a key) -> O(1)
    - Rank (i.e., # of keys less than or equal to a given value) -> O(log n)
    - Output in Sorted Order (i.e., smallest to largest) -> O(n)
    - Insert -> O(n)
    - Delete -> O(n)

- Raise D'Etre: Like sorted array + fast (logarithmic) inserts + deletes!

- Balanced Binary Tree
    - Search (Binary Search) -> O(log n)
    - Selection (given order statistic i) -> O(log n)
    - Min / Max -> O(log n)
    - Predecessor / Successor (given pointer to a key) -> O(log n)
    - Rank (i.e., # of keys less than or equal to a given value) -> O(log n)
    - Output in Sorted Order (i.e., smallest to largest) -> O(n)
    - Insert -> O(log n)
    - Delete -> O(log n)

- If you ONLY need min/max, insert, delete -> consider using a HEAP instead.
- If you ONLY need search, insert, delete -> consider using a HASH TABLE
  instead.

### Balanced Search Tree - Basics

- Exactly one node per key
- Most basic version:
    - Each node has:
        - Left child pointer
        - Right child pointer
        - Parent pointer

- Search tree property:
    - All keys to the left, should be less.
    - All keys to the right, should be more.
    - Holds at every single node in the tree.

- Height (aka depth, longest root-leaf path) could be anywhere form ~= log n
  to ~= n
    - Best case -> perfectly balanced

- To SEARCH for a key k in tree T:
    - start at the root
    - traverse left/right child pointers as needed
        - left if k < key, right if k > key
    - return node with key k or NULL, as appropriate

- To INSERT a new key k into a tree T:
    - search for k (unsuccessfully)
    - rewire final NULL pointer to point to a new node with key k

- Worst-case running time of Search/Insert is O(height).

Operations that Search trees support (but not heap/hash tables do not):

- To compute the MINIMUM/MAXIMUM key of a tree:
    - start at the root
    - follow left/right child pointers until you can't anymore
    - return last key found

- To compute the PREDECESSOR of key k:
    - easy case: if k's left subtree non-empty
        - return max key in left subtree
    - otherwise:
        - follow parent pointer until you find a key smaller than your own (
          first time you take a left turn)

- To PRINT OUT keys in increasing order:
    - let r = root of the search tree, with subtrees T_l and T_r
    - recurse on T_l
        - by recursion/induction, prints out keys of T_l in increasing order
    - print out r's key
    - recurse on T_r
        - print's out keys of T_r in increasing order
    - Running Time: O(n)

- To DELETE a key k from a search tree:
    - SEARCH for k
    - EASY CASE (k's node has no children):
        - just delete k's node from the tree, done
    - MEDIUM CASE (k's node has one child):
        - just "splice out" k's node (unique child assumes position previous
          held by k's node)
    - DIFFICULT CASE (k's node has two children):
        - compute k's PREDECESSOR l
            - i.e. traverse k's (non-NULL) left child pointer, then right child
              pointers until no longer possible
        - SWAP k and l
        - DELETE k's new node
    - Running Time: O(height)

- SELECT & RANK
    - Idea: store a bit of extra info at each tree node about the tree itself (
      i.e. not about the data)
    - Example Augmentation:
        - size(x) = # of tree nodes in subtree rooted at x
    - If x has children y and z, then size(x) = size(y) + size(z) + 1
    - Also: easy to keep sizes up-to-date during an Insertion or Deletion

- How to SELECT ith order statistic from augmented search tree (with subtree
  sizes):
    - start at root x, with children y and z
    - let a = size(y)  [a=0 if x has not left child]
    - if a = i - 1, return x's key
    - if a >= i, recursively compute ith order statistic of search tree rooted
      at y
    - if a < i - 1, recursively compute (i - a - 1)th order statistic of search
      tree rooted at z
    - Running Time = O(height)

### Red-Black Trees

- Idea: ensure that height is always O(log n) [best possible]
    - Search / Insert / Delete / Min / Max / Pred / Succ will then run in O(log
      n) time [n = # of keys in tree]

- Example: Red-Black trees [Bayer '72]
    - See also -> AVL trees, splay trees, B trees

- Red-Black Invariants:
    - Each node red or black
    - Root is black
    - No 2 reds in a row [red node => only black children]
    - Every root-NULL path has same number of black nodes

- Claim: A chain of length 3 cannot be a red-black tree.

- Claim: Every red-black tree with n nodes has height <= 2 log 2 (n + 1)
- Proof:
    - Observation: if every root-NULL path has >= k nodes, then tree includes (
      at the top) a perfectly balanced search tree of depth k - 1
    - Size n of the tree must be at least 2^k - 1, where k = minimum # of
      nodes on root-NULL path
        - k <= log 2 (n + 1)
        - Thus, in a red-black tree with n nodes, there is a root-NULL path with
          at most log 2 (n + 1) black nodes.
    - By 4th Invariant:
        - Every root-NULL path has <= log 2 (n + 1) black nodes.
    - By 3rd Invariant:
        - Every root-NULL path has <= 2 log 2 (n + 1) total nodes.
