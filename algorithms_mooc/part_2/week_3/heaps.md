### Data Structures

- Point:
    - Organize data so that it can be accessed quickly and usefully.

- Examples:
    - lists, stacks, queues, heaps, search trees, hash tables, bloom filters, union-find, etc.

- Why so many?
    - Different data structures support different sets of operations.
      -> Suitable for different types of tasks

- Rule of Thumb:
    - Choose the "minimal" data structure that supports all the operations you need, but no superfluous ones.

Level 0 - "What's a data structure?"
Level 1 - cocktail party-level literacy
Level 2 - "this problem calls for a heap"
Level 3 - "I only use data structures that I wrote myself"

### Heap: Operations and Applications

- A container for objects that have keys
    - Key/Value -> SIN #/Employee records, Weight of Edge/Network Edges, Time to Occur/Event

- Supported Operations:
    - INSERT: add a new object to the heap.
        - Running Time: O(log n)
    - EXTRACT-MIN or EXTRACT-MAX: Remove an object in heap with a minimum/maximum key value.
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
        - objects = event records [action/update to occur at a given time in the future]
        - key = time event scheduled to occur
        - Extract-Min => yields the next scheduled event

    - Median Maintenance
        - I give you: a sequence x_1, ..., x_n of numbers, one-by-one.
        - You tell me: at each time step i, the median of { x_1, ..., x_i }.
        - Constraint: use O(log i)
        - Solution:
            - Maintain heaps H_low (w/ extract-max) and H_high (w/ extract-min)
        - Key idea:
            - Maintain invariant that ~= i/2 smallest (largest) elements in H_low (H_high)
            - If new number is less than max of H_low, add to H_low
            - If new number is greater than min of H_high, add to H_high
            - If there is imbalance b/w H_low and H_high, extract and insert into other heap
            - Median:
                - If i is even, either max of H_low and min of H_high
                - If i is odd, extract element from heap with additional element

    - Speeding up Dijkstra's Shortest Path Algorithm:
        - Naive implementation => runtime = O(n * m)
            - n = # of loop iterations
            - m = work per iteration (linear scan through edges for minimum computation)
            - with heaps => run time = O(m log n)

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
- If you ONLY need search, insert, delete -> consider using a HASH TABLE instead.

### Balanced Search Tree - Basics

- Exactly one node per key
- Most basic version:
    -  Each node has:
        - Left child pointer
        - Right child pointer
        - Parent pointer
         
- Search tree property: 
    - All keys to the left, should be less.
    - All keys to the right, should be more.
    - Holds at every single node in the tree.


Binary Search Tree Basics, Part 1 - 6:51