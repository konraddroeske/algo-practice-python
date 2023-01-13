### Single-Source Shortest Path Problem

- Input: directed graph G = (V, E), edge length c_e for each e in E, source 
  vertex s in V.
    - Can assume no parallel edges.

- Goal: for every destination v in V, compute the length of a shortest s-v path.
    - sum of edge costs

- On Dijkstra's Algorithm:
    - Good news: O(m log n) running time using heaps.
        - m = number of edges
        - n = number of vertices
    - Bad news: 
        - not always correct with negative edge lengths [e.g. edges <--> 
          financial transactions]
        - not very distributed (relevant for internet routing)

- Solution: the Bellman-Ford Algorithm

- Question: how to define shortest paths when G has a negative cycle?
 
- Solution #1: compute the shortest s-v path, with cycles allowed.
- Problem: undefined (or -infinity) [will keep traversing negative cycle]
     
- Solution #2: compute the shortest cycle-free s-v path
- Problem: NP-hard (no polynomial algorithm, unless P = NP)

- Solution #3: (for now) assume input graph has no negative cycles.
- Later: will show how to quickly check this condition

### The Bellman-Ford Algorithm

- Goal: either,
    - for all destinations v in V, compute the length of a shortest s-v  path
    - output a negative cycle

- Optimal Substructure:
    - Intuition:
        - exploit sequential nature of paths sub-path of a shortest path 
          should itself be shortest.
    - Issue:
        - not clear how to define "smaller" and "larger" sub-problems
    - Key idea:
        - artificially restrict the number of edges in a path

- Lemma: Let G = (V, E) be a directed graph with edge lengths c_e and source 
  vertex s. 
    - G might or might not have a negative cycle
    - For every v in V, i in {1, 2, 3, ...}, let P = shortest s-v path with at 
      most i edges
    - Case 1:
        - i in P has <= (i - 1) edges, it is a shortest s-v path with <= (i - 1)
          edges
    - Case 2:
        - if P has i edges with the last hop (w, v), then P' is a shortest 
          s-w path with <= (i - 1) edges

- Proof by Optimal Substructure: 
    - Case 1: by (obvious) contradiction
    - Case 2: if Q is shorter than P', then Q + (w, v) is shorter than P' + 
      (w, v), which contradicts the optimality of P.

- Notation: Let L_i_v = minimum length of a s-v path with <= i edges.
    - with cycles allowed
    - defined as + infinity if no s-v paths with <= i edges
- Recurrence:
    - For every v in V, i in {1, 2, 3, ...}
    - case_1 = L_(i-1)_v
    - case_2 = min (w, v) in E { L_(i-1)_w + c_w_v }
    - L_i_v = min { case_1, case_2 }

    - Correctness: brute-force search from the only (1 + in-degree(v)) 
      candidates (by the optimal substructure lemma).

- Now: suppose input graph G has no negative cycles.
    - shortest paths do not have cycles (removing a cycle only decreases length)
    - have <= (n - 1)  edges

- Point: if G has no negative cycle, only need to solve sub-problems up to i 
  = n - 1
- Sub-problems: compute L_i_v for al i in {0, 1, 2, ..., n - 1}

- Let A = 2-D array (indexed by i and v)
    - Base case:


The Basic Algorithm I - 6:30
