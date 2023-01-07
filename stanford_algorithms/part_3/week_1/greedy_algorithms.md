## Applications

### Graphs and the Internet

- Claim: the Internet is a graph
    - vertices = end hosts and routers
    - directed edges = direct physical or wireless connections

- Other graphs related to the Internet:
    - Web graph (vertices: web pages, edges: hyperlinks)
    - Social networks (vertices: people, edges: friends/follow relationship)

### Internet Routing

- Bellman-Ford Algorithm:
    - Shortest path algorithm that uses only local computation (as opposed to
      Dijkstra's)

### Sequence Alignment

- Fundamental problem in computational genomics.
- Input: Two strings over the alphabet (portions of one or more genomes)
- Problem: Figure out how "similar" the two string are.
- Example applications:
    1. Extrapolate function of genome substrings.
    2. Similar genomes can reflect proximity in evolutionary tree.

- Question: What does "similar" mean?
- Intuition: AGGGCT, AGGCA are similar because they be "nicely aligned".
- Idea: measure similarity via quality of "best" alignment.
- Assumptions: have experimentally determined penalties for gaps and the
  possible matches.

Problem Statement

- Input: 2 string over { A, C, G, T }
    - Penalty pen_gap >= 0 for each gap
    - Penalty pen_at >= 0 for mismatching A & T
    - etc.

- Output: alignment of the strings that minimizes the total penalty.
    - Called the Needleman-Wunsch score
    - Small N-W score ~= similar strings

### Algorithms are fundamental

- Note: this measure of genome similarity would be useless without an
  efficient algorithm to find the best alignment.
- Brute Force Search: try all possible alignments, remember the best one.
- Question: suppose each string has length 500. Roughly how many possible
  alignments are there?
    - > = 2^500 possible alignments

### Greedy Algorithms

- Algorithm Design: no single "silver bullet" for solving problems.
- Some design paradigms:
    - divide and conquer (merge sort)
    - randomized algorithms (quick sort w/ random pivot)
    - greedy algorithms (dijkstra's shortest path)
    - dynamic programming

- "Definition": iteratively make "myopic" decisions, hope everything works
  out at the end.
- Example: Dijkstra's shortest path algorithm
    - Processed each destination once, irrevocably

- Contrast w/ Divide and Conquer
    1. Easy to propose multiple greedy algorithms for many problems
    2. Easy running time analysis (contrast with Master Method, etc.)
    3. Hard to establish correctness (contract with straightforward inductive
       correctness proofs)

- Danger: Most greedy algorithms are NOT correct (even if your intuition
  says otherwise!)

### Proofs Of Correctness

- Method 1: Induction ("greedy stays ahead")
    - Example: Correctness proof for Dijkstra's algorithm
- Method 2: "Exchange Argument"
- Method 3: Whatever works!

### Application: Optimal Caching

- The Caching Problem:
    - small fast memory (the cache)
    - big slow memory
    - process sequence of "page requests"
    - on a "fault" (that is, a cache miss), need to evict something from
      cache to make room - but what?

- Cache: [a, b, c, d]
- Request sequence: c (good) -> d (good) -> e (page fault, remove a) -> f
  (page fault, remove b) -> a (page fault) -> b (page fault)
    - 4 page faults
        - 2 were inevitable
        - 2 were consequences of poor eviction choices
            - should have evicted c & d instead of a & b

### The Optimal Caching Algorithm

- Theorem: The "furthest-in-future" algorithms is optimal (i.e., minimizes
  the number of cache misses)

- Why useful?
    1. Serves as guideline for practical algorithms
        - e.g. Least Recently Used (LRU) should do well provided data
          exhibits locality of reference
    2. Serves as an idealized benchmark for caching algorithms

- Proof: tricky exchange argument

### Schedule Problem

- Setup: One shared resource (e.g., a processor)
    - Many jobs to do (e.g. processes)
- Question: in what order should we sequence the jobs?
- Assume: Each job j has a:
    - weight w_j ("priority")
    - length l_j ("how long job will take")

- Completion Times
    - Definition: the completion time (c_j) of a job_j = sum of job lengths up
      to and including j.
    - Example:
        - 3 jobs, l_1 = 1, l_2 = 2, l_3 = 3
    - Question: What is c_1, c_2, c_3 if jobs completed in order?
        - 1, 3, 6

- The Objective Function
    - Goal: minimize the weighted sum of completion times.
        - Min (Sum n j=1) w_j * c_j

### The Algorithm

- Recall: want to min (Sum n j=1) w_j * c_j
- Goal: Devise a correct greedy algorithm
- Question:
    1. with equal lengths, schedule larger or smaller-weight jobs earlier?
        - Larger
    2. with equal weights, schedule shorter or longer earlier?
        - Shorter

- What if w_i > w_j but l_i > l_j?
    - Idea: assign "scores" to jobs that are:
        - Increasing in weight
        - Decreasing in length
    - Guess:
        1. Order jobs by decreasing value of w_j - l_j
        2. Order w_j / l_j
    - Breaking a greedy algorithm:
        - To distinguish b/w 1 and 2: find an example where the two
          algorithms produce different outputs (at least one will be incorrect)

- So: Algo #1 not (always) correct.
- Claim: Algo #2 (order by decreasing ratio w_j / l_j) is always correct.

- Proof: by an Exchange Argument
- Plan: Fix arbitrary input of n job.
    - will proceed by contradiction
    - let s = greedy schedule, s* = optimal schedule
    - will produce schedule even better than s*, contradicting purported
      optimality of s*

- Assume:
    - all w_j / l_s distinct
    - w_1 / l_1 > w_2 / l_2 > ... > w_n / l_n
- Thus:
    - greedy schedule s is just 1, 2, 3, ..., n
    - If optimal schedule s* != s, then there are consecutive jobs i, j with
      i > j
        - Only schedule where indices always go up is 1, 2, 3, ..., n
- So far:
    1. w_1 / l_1 > w_2 / l_2 > ... > w_n / l_n
    2. in optimal s*, there exists consecutive jobs i, j with i > j

- Thought Experiment: suppose we exchange order of i & j in s* (leaving
  other jobs unchanged):
    - i completion time goes up
    - j completion time goes down
    - any other job k is unaffected
- Upshot:
    1. Cost of exchange w_i * l_j [c_i goes up by l_j]
    2. Benefit of exchange w_j * l_i [c_j goes up by l_i]

- Note:
    - i > j => w_i / l_i < w_j / l_j
    - => w_i * l_j < w_j * l_i
    - cost < benefit
    - => swap improves s*, contradicts optimality of s*
    - QED

### Minimum Spanning Trees

- Informal Goal: connect a bunch of points together as cheaply a possible.
- Applications:
    - clustering
    - networking
- Blazingly fast greedy algorithms:
    - Prim's Algorithm
    - Kruskal's Algorithm
    - O(m log n) time
        - Using suitable data structures

- Problem Definition:
    - Input: undirected graph G = (V, E) and cost c_e for each edge e in E.
        - assume adjacency list representation
        - ok if edge costs are negative
    - Output: minimum cost tree T, that spans all vertices (i.e. sum of edge
      costs)
        1. T has no cycles
        2. the subgraph (V, T) is connected (i.e. contains path b/w each pair
           of vertices)

- Standing Assumptions:
    1. input graph G is connected
        - else no spanning trees
        - easy to check in preprocessing (e.g. depth-first search)
    2. Edge costs are distinct
        - Prim + Kruskal remain correct with ties (which can be broken
          arbitrarily)

## Prim's MST Algorithm

- initialize X = [s] [s in V chosen arbitrarity]
- T = empty [invariant: X = vertices spanned by tree-so-far T]
- while X != V:
    - let e = (u, v) be the cheapest edge of G with u in X and v not in X
    - add e to T
    - add v to X
    - i.e., increase # of spanned vertices in the cheapest way possible

Theorem: Prim's algorithm always computes the MST

### Claim 1: Prim's algorithm outputs a spanning Tree T*

- Definition: a cut of a graph G = (V, E) is a partition of V into 2
  non-empty sets.

- Empty Cut Lemma: a graph is *not* connected <==> there exists (A, B) with
  *no* crossing edges
- Proof:
    - Assume the RHS. Pick any u in A and v in B.
        - Since no edges cross (A, B), there is no u-v path in G.
        - G not connected!
    - Assume the LHS. Suppose G has no u-v path.
        - Define A = {vertices reachable from u in G} (i.e. u's connected
          component)
        - B = {all other vertices} (i.e. all other connected components)
        - Note: no edges cross the cut (A, B)

- Double-Crossing Lemma:
    - Suppose the cycle C has an edge crossing the cut (A, B):
        - Then so does some other edge of C

- Lonely Cut Corollary:
    - if e is the only edge crossing some cut (A, B), then it is not in any
      cycle

- Proof:
    1. Algorithm maintains invariant that T spans X (straightforward induction)
    2. Can't get stuck with X != V
        - otherwise the cut (X, V-X) must be empty, by empty cut lemma input
          graph G is disconnected
    3. No cycles ever get created in T:
        - Consider any iteration, with current sets X and T. Suppose e gets
          added.
        - keypoint: e is the first edge crossing (X, V-X) that gets added to T
            - addition cannot create a cycle in T (by lonely cut corollary)

### Claim 2: T* is an MST

- Key question: when is it "safe" to include an edge in the tree-so-far?
- *Cut Property*:
    - Consider an edge e of G.
    - Suppose there is a cut (A, B) such that e is the cheapest edge of G
      that crosses it.
    - Then e belongs to the MST of G

- Claims: Cut Property => Prim's algorithm is correct
- Proof: By previous video, Prim's algorithm outputs a spanning tree T*.
- Key point: every edge e in T* is explicitly justified by the Cut Property
  justified by the Cut Property.
    - => T* is a subset of the MST
    - => since T* is already a spanning tree, it must be MST

### Fast Implementation

- Naive Implementation:
    - initialize X = [s] [s in V chosen arbitrarity]
    - T = empty [invariant: X = vertices spanned by tree-so-far T]
    - while X != V:
        - let e = (u, v) be the cheapest edge of G with u in X and v not in X
        - add e to T
        - add v to X
        - i.e., increase # of spanned vertices in the cheapest way possible

    - Running time:
        - O(n) iterations [where n = # of vertices]
        - O(m) time per iteration [where m = # of edges]
        - => O(m * n) time


- Speed-up via Heaps
    - Specifically: a heap supports Insert, Extract-Min, and Delete in O(log n)
      time
    - Natural idea: use heap to store edges, with keys = edge costs.
    - Exercise: leads to an O(m log n) implementation of Prim's algorithm.

- Invariant #1: Elements in heap = vertices of V - X
- Invariant #2: for v in V - X, key[v] = the cheapest edge (u, v) with u in X

- Check: can initialize heap with O(m + n log n) = O(m log n) preprocessing.
    - O(m) to compute key
    - O(n log n) for inserts
    - m >= n - 1, therefore bounded above by O(m log n)

- Note: given invariants, Extract-Min yields next vertex v not in X and edge
  (u, v) crossing (X, V - X) to add to the X and T, respectively.

- Issue: might need to recompute some keys to maintain invariant #2 after
  each Extract-Min.
- Pseudocode: when v added to X:
    - for each edge (v, w) in E:
        - if w in V - X:
            - Delete w from heap
                - think through bookkeeping needed to pull this off
            - recompute key[w] := min[key[w], C_vw]
            - re-insert w into heap

- Running Time w/ Heaps
    - dominated by time required for heap operations
    - (n - 1) Inserts during preprocessing
    - (n - 1) Extract-Min (one per iteration of while loop)
    - Each edge (v, w) triggers one Delete/Insert combo
        - when its first endpoint gets sucked into X
    - => O(m) heap operations (m >= n - 1 since G connected)
    - => O(m log n) time