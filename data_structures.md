### Array

- Insertion/Deletion requires moving all the contents of the array in order to
  preserve the elements of the array

- Memory
    - Arrays represent data with little overhead.
    - Memory is more rigid

### Linked List

- Node consists of:
    - Data
    - Next:
        - Address and memory of next node in chain

- Traversing a linked list:
    - Start at head node
    - Move to the next node

- Searching a linked list is essentially traversing the list in sequence

- Each node can be anywhere in memory:
    - The pre-fetcher might not be able to cache ahead of time
    - There is potential for cache miss with every element
    - Array is easier to process

- Inserting/Deleting is trivial, but you need a fast way to getting to the node.

- Memory
    - Required more memory than arrays
    - There is more flexibility, where memory can go in between used sections

- When to use?
    - Practically not used very often except for optimizations.

### Set

- Unordered
- Mutable
- Does not allow duplicate elements

- Built-in functions:
    - Union: Combined elements from sets without duplication
    - Intersection: Takes elements that exist in both sets
    - Difference: Takes elements from first set that are not in the second set
    - Symmetric Difference: Returns all elements from A and B that do not
      intersect

    - Update: Adds elements from second set to first set w/o duplicates
    - Intersection Update: Updates first set with elements only found in both
      sets
    - Difference Update: Updates first set by removing elements from second set
    - Symmetric Difference Update: Updates first set by removing shared
      elements, and keeping the rest

    - issubset: Returns True if all elements in first set are in second set
    - isuperset: Returns True if first set contains all the elements from second
      set
    - isdisjoint: Return True if no elements are shared

