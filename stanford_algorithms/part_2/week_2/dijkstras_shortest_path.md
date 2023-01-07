### Dijkstra's Shortest Path

Input: Directed Graph G = (V, E) (m = |E|, n = |V|)

- each edge had non-negative length l_e
- source vertex s

Output: for each v in V, compute,
L(v) := length of the a shortest s-v path in G

Assumptions:

1. [for convenience] for all v in V, there exists an s -> v path
2. [important] l_e >= 0 for all e in E

- Question: Doesn't BFS already compute the shortest path?
    - Yes, IF l_e = 1 for every edge e


- Question: Why not just replace each edge e by directed path of l_e unit length edges?
    - l_e = 3 -> 3 * l_e = 1
    - Blows up graph too much.
    - Solution: Dijkstra's shortest path algorithm

### Pseudocode:

- Initialize:
    - X = [s] [vertices processed so far]
    - A[s] = 0 [computed shortest path distances]
    - B[s] = empty path [computed shorted path] - DO NOT INCLUDE IN ACTUAL IMPLEMENTATION

- Main Loop:
    - while X != V: (need to grow X by one node)
        - among all edges (v, w) in E, with v in X, w not in X, we pick one that minimizes:
            - A[v] + l_vw (Dijkstra's greedy criterion)
            - Call it (v*, w*)
        - add w* to X
        - set A[w*] := A[v*] + l_v*w*
        - set B[w*] := B[v*] u (v*, w*)

### Dijkstra's Algorithm: Examples

### Correctness of Dijkstra's Algorithm

A[v] = L(v) for all v in V
A[v] -> what algorithm computes
L[v] -> true shortest path distance s to v

### Dijkstra's Algorithm: Implementation and Running Time

- Naive Implementation:
    - (n - 1) iterations of the while loop
    - O(m) work per iteration
    - O(1) work per edge
    - O(m * n) running time

- Heap Operations:
    - Heap = perform insert, extract-min in O(log n) time.
    - Conceptually, a perfectly balanced binary tree
        - Height ~= log 2 n
    - Heap property: at every node, key <= children's keys
    - Extract-min by swapping up last leaf, bubbling down
    - Insert via bubbling up
    - Also, will need ability to delete from middle of heap, bubble up or down as needed

- Two Invariants:
    - Invariant #1:
        - elements in heap = vertices of V - X
    - Invariant #2:
        - for v not in X, key[v] = the smallest Dijkstra greedy score of an edge (u, v) in all Edges (E) with u in X
        - for any v without edge terminating in V - X, score is +infinity
    - Point: by invariants, Extract-Min yields correct vertex w* to add to X next
        - and we set A[w*] to key[w*]

- To Maintain Invariant #1:
    - By definition, vertices that remain in the heap are the ones we haven't processed yet, and the ones outside of X.

- To Maintain Invariant #2:
    - When w extracted from heap (i.e. added to X)
        - For each edge (w, v) in E:
            - if v in V - X (i.e in heap):
                - delete v from heap
                - recompute key[v] = min[key[v], A[w] + l_wv]
                - re-insert v into heap

- Running Time: Dominated by heap operations (O(log n) each)
    - (n - 1) Extract-min
    - each edge (v, w) triggers at most one Delete/Insert combo
        - if v added to X first
    - So, # of heap operations is O(n + m) = O(m)
        - Since graph weakly connected
    - So, running time O(m log n) (like sorted, rather than O(m * n))