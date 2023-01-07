### MST Review

- Input: undirected graph G = (V, E), edge costs c_e
- Output: min-cost spanning tree (no cycles, connected)
- Assumptions: G is connected, distinct edge costs.
- Cut Property: if e is the cheapest edge crossing some cut (A, B), then e
  belongs to the MST.

### Kruskal's Algorithm

- Sort edges in order of increasing cost [rename edges 1, 2, 3, ..., m] -> O(m
  log n)
- T = [] (Tree in progress)
- for i = 1 to m -> O(m) iterations
    - if T u { i } has no cycles -> O(n) time to check for cycle [check if
      path b/w (u, v) using BFS or DFS in the graph T (contains <= n - 1
      edges)]
        - add i to T
- return T

Theorem: Kruskal's algorithm is correct
Proof: Let T* = output of Kruskal's algorithm on input graph G

1. Clearly T* has no cycles

2. T* is connected. Why?
   a. By Empty Cut Lemma, only need to show that T* crosses every cut
   b. Fix a cut (A, B). Since G connected, at least one of its edges crosses
   (A, B).
   Key point: Kruskal will include first edge crossing (A, B) that it sees [by
   lonely cut corollary, cannot create a cycle]

3. Every edge of T* justified by the cut property (implies T* is the MST)
    - Reason: Consider iteration where edge (u, v) added to the current set T.
    - Since T u { (u, v) } has no cycle, T has no u-v path
    - => There exists empty cut (A, B) separating u and v
    - => by 2b, no edges crossing (A, B) were previously considered by
      Kruskal's algorithm
    - => (u, v) is the first (+ hence the cheapest) edge
    - => (u, v) justified by the Cut Property

### Union-Find

- Running Time of Straightforward Implementation:
    - O(m log n) + O(m * n) -> O(m * n)
    - Plan:
        - Data structure for O(1) cycle check => O(m log n) time

- Raison D'etre of a union-find data structure: maintain partition of a set
  of objects.
 
- Operations:
    - Find(x): Return the name of the group to which the object belongs.
    - Union(c_i, c_j): Fuse groups c_i and c_j into a single one.

- Why useful for Kruskal's algorithm?
    - Objects = vertices
    - Groups = connected components wrt currently chosen edges T
    - adding new edge (u, v) to T <==> fusing connected components of u, v

- Idea #1:
    - maintain one linked structure per connected component of (V, T)
    - each component has an arbitrary leader vertex.
- Invariant:
    - each vertex points to the leader of its component ["name" of a
      component inherited from leader vertex]
- Key Point:
    - given edge (u, v), can check if u & v already in some component in O(1)
      time [if and only if leader pointers of u, v match]
    - i.e., FIND(u) = FIND(v)
    - => O(1) time cycle checks!
- Note: when new edge (u, v) added to T, connected components of u & v merge
    - Worst case leader pointer updates O(n) (not great)

- Idea #2:
    - when two components merge, have smaller one inherit the leader of the
      larger one [easy to maintain the size field in each component to
      facilitate this]
    - Worst case on leader pointer updates is O(n)

- But:
    - How many times does a single vertex have its leader pointer update
      over the course of Kruskal's algorithm?
        - O(log n)
        - Reason: every time v's leader pointer gets updated, population of
          its component at least doubles => can only happen <= log 2 n times!

- Scorecard:
    - O(m log n) time for sorting
    - O(m) time for cycle checks [O(1) per iteration]
    - O(n log n) time overall for leader pointer updates
    - Overall => O(m log n) total (as sorting is the bottleneck)

### Clustering

- Informal goal: given n "points" [web pages, images, genome fragments, etc.]
  classify into "coherent groups".
    - aka "unsupervised learning"
- Assumptions:
    1. as input, given (dis)similarity measure - a distance(p, q)
       between point pair.
    2. symmetric [i.e., d(p, q) = d(q, p)]

- Examples: Euclidian distance, genome similarity, etc.
- Goal: Same cluster <==> "nearby"

### Max-Spacing k-Clusterings

- Assume: we know k := # of clusters desired
    - In practice, can experiment with a range of values
    - all points p & q separated if they're assigned to different clusters.

- Definition: the spacing of a k-clustering is min separated p, q d(p, q)
    - the bigger, the better

- Problem statement: given a distance measure d and k, compute the
  k-clustering with maximum spacing.

### A Greedy Algorithm

- Initially, each point in a separate cluster
- Repeat until only k clusters:
    - let p, q = closest pair of separated points
        - determines the current spacing
    - merge the clusters containing p & q into a single cluster

- Note: just like Kruskal's MST algorithm, but stopped early.
    - points <==> vertices; distances <==> edge costs; point pairs <==> edges
    - called "Single-Link Clustering"

- Correctness Claim:
    - Theorem: single-link clustering finds the max-spacing k-clustering.
- Proof:
    - Let c_1, ..., c_k = greedy clustering with spacing S
    - let c_hat_1, ..., c_hat_k = arbitrary other clustering
- Need to show:
    - spacing of c_hat_1, ..., c_hat_k is <= S

- Case 1: c_hat_i's are the same as the c_i's [maybe after renaming] => has
  the same spacing S
- Case 2: otherwise, can find a point pair p, q such that:
  a) p, q in the same greedy cluster c_i
  b) p, q in different cluster c_hat_i, c_hat_j

- Property of greedy algorithm: if two points x, y "directly merged" at some
  point, then d(x, y) <= S
    - distance b/w merged point pairs only goes up

- Easy case: if p, q directly merged at some point, S >= d(p, q) >= spacing
  of c_hat_1, ..., c_hat_k

- Tricky case: p, q "indirectly merged" through multiple direct merges.
    - let p, a_1, ..., a_l, q be the path of direct greedy merges connecting
      p & q
    - Key point: Since p in c_hat_i and q not in c_hat_i, there exists
      consecutive pair a_j, a_(j + 1) with a_j in c_hat_i, a_(j+1) not in
      c_hat_i
    - => S >= d(a_j, a_(j + 1)) >= spacing of c_hat_i, ..., c_hat_k
