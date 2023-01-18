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
    - Base case: A[0, s] = 0; A[0, v] = +infinity for all v != s
    - For i = 1, 2, 3, ..., n - 1
        - For each v in V:
            - case_1 = A[i - 1, v]
            - case_2 = min (w, v) in E { A[i - 1, w] + c_w_v }
            - A[i, v] = min(case_1, case_2) 
    -  As discussed: if G has no negative cycle, then algorithm is correct.
        - with final answers = A[n - 1, v]'s 


- Running Time: O(m * n)
- In any directed graph, m is the sum of the in-degrees.

- Optimizations:
    - Stopping Early
        - Suppose for some j < n - 1, A[j, v] = A[j - 1, v] for all vertices v
        - for all v, all future A[i, v]'s will be the same
        - can safely halt

- Stopping Negative Cycles
   - Question: What if the input graph G has a negative cycle? 
       - want algorithm to report this fact
   - Claim:
       - G has no negative-cost cycle IFF in the (extended) Bellman_form 
         algorithm, A[n - 1, v] = A[n, v] for all v in C (extra iteration)
   - Consequence:
       - can check for a negative cycle just by running Bellman-Ford for an 
         extra iteration (running time still O(m * n))
   - Edge case:
        - If shortest path distances are NOT finite (if s has no outgoing 
          arcs), then left hand side is false while right hand is satisfied
        - G must have a negative cost cycle that is reachable from source 
          vertex S
    - Proof of Claim:
        - Right Side: already proved in correctness of Bellman-Ford
        - Left Side: Assume A[n - 1, v] = A[n, v] for all v in V
            - assume also these are finite (< +infinity)
        - Let d(v) denote the common value of A[n - 1, v] and A[n, v]
        - Recall: A[n, v] = min (case_1, case_2)
            - case_1 = A[n - 1, v]
            - case_2 = min (w, v) in E { A[n - 1, w] + c_w_v }
            - d(v) = A[n, v], d(w) = A[n - 1, w]
        - Thus: d(v) <= d(w) + c_w_v for all edges (w, v) in E
        - Equivalently: d(v) - d(w) <= c_w_v
        - Now: consider an arbitrary cycle C 
            - sum [(w, v) in C] c_w_v >= sum [(w, v) in C] (d(w) - d(v)) = 0


- Space Optimization:
    - Current space: O(n^2)
        - O(1) for each n^2 sub-problems
    - Predecessor Pointers
        - All values we care about are from the last iteration
        - We can throw out all previous rounds of sub-problems
    - Note: only need the A[i - 1, v]'s to compute the A[i, v]'s
        - Only need O(n) to remember the current and last rounds of sub-problems
        - Only O(1) per destination
    - Drawbacks
        - If you want the optimal solution, and not just the value, then you 
          need all data to reconstruct.
    - Concern: without a filled-in table, how do we reconstruct the shortest 
      paths?
    - Idea:
        - Compute a second table B, where B[i, v] = 2nd-to-last vertex on a 
          shortest s -> v path with <= i edges. (or NULL if not such paths 
          exist)
            - "predecessor pointers"
    - Reconstruction: 
        - Assume the input graph G has no negative cycles and we correctly 
          compute the B[i, v]'s
    - Then: tracing back predecessor pointers = the B[n - 1, v]'s - from v 
      to s yields a shortest s-v path
        - B[n - 1, v] = last hop of a shortest s-v path
        - correctness from optimal substructure of shortest paths

- Computing predecessor pointers:
    - Recall:
        - case_1 = A[i - 1, v]
        - case_2 = min (w, v) in E { A[i - 1, w] + c_w_v }
        - A[i, v] = min(case_1, case_2) 
    - Base Case:
        - B[0, v] = null for all v in V
    - To compute B[i, v] with i > 0:
        - if case_1, B[i, v] = B[i - v, v]
        - if case_2, B[i, v] = the vertex w achieving the minimum (i.e., the 
          new last hop)
    - Correctness:
        - computation of A[i, v] is brute-force search through the (1 + in-deg(v)
          ) possible optimal solutions, B[i, v] is just caching the last hop of 
          the winner.
    - To reconstruct a negative-cost cycle:
        - use DFS to check for a cycle of predecessor pointers after each 
          round (must be a negative cost cycle).


## All Pairs Shortest Paths

- Input: directed graph G = (V, E) with edge costs c_e for each e in E.
    - no distinguished source vertex
- Goal:
    - compute the length of a shortest u -> v path for all pairs of vertices 
      u, v in V
    - OR, correctly report that G contains a negative cycle
- Running time (non-negative edge costs):
    - n * Dijkstra = O(n * m *  log n)
        - Sparse Graph: O(n^2 log n) if m = O(n)
        - Dense Graph: O(n^3 log n) if m = O(n^2)
- Running time (general edge costs):
    - n * Bellman-Ford = O(n^2 * m)
        - Sparse Graph: O(n^3) if m = O(n)
        - Dense Graph: O(n^4) if m = O(n^2)


- Floyd-Warshall Algorithm
    - Running time: O(n^3) algorithm for all pairs shortest paths.
    - Works even with graphs with negative edge lengths. 
    - Thus: 
        - (1) at least as good as n Bellman-Fords, better in dense graphs.
        - (2) in graphs with non-negative edge costs, competitive with n 
          Dijkstra's in dense graphs.
    - Important Special Case:
        - Transitive closure of a binary relation.
        - i.e., all pairs reachability
    - Open question:
        - solve APSP significantly faster than O(n^3) in dense graphs?

- Optimal Substructure:
    - Recall: can be tricky to define ordering on sub-problems in graph 
      problems.
    - Key Idea: order the vertices V = {1, 2, 3, ..., n} arbitrarily.
        - Let V(k) = {1, 2, ..., k}
    - Lemma: Suppose G has no negative cycle. 
        - Fix source i in V, destination j in V, and k in {1, 2, ..., k}
        - Let P = shortest (cycle-free) i-j path with all internal nodes in V(k).
         
- Optimal Substructure Lemma:
    - Suppose G has no negative cost cycle. Let P be a shortest (cycle-free) 
      i-j path with all internal nodes in V(k). Then:
        - case_1: if k not internal to P, then P is a shortest (cycle-free) 
          i-j path with all internal vertices in V(k-1)
        - case_2: if k is internal to P, then: (i) -- p_1 --> (k) -- p_2 --> (j)
            - p_1 = shortest (cycle-free) i-k path with all internal nodes 
              in V(k-1) 
            - p_2 = shortest (cycle-free) k-j path with all internal nodes 
              in V(k-1)
    - Proof: Similar to Bellman-Ford

### The Floyd-Warshall Algorithm

- Setup: Let A = 3-D array (indexed by i, j, k)
- Intent: A[i, j, k] = length of a shortest i-j path with all internal 
  nodes in {1, 2, ..., k}
- Base cases: 
    - for all i, j in V, if k == 0:
        - case_1 = 0 if i == j
        - case_2 = c_ij if (i, j) share edge
        - case_3 = +infinity if i != j and (i, j) do not share edge
        - A[i, j, 0] = case_1 or case_2 or case_3
- for k = 1 in n:
    - for i = 1 to n:
        - for j = 1 to n:
            - case_1 = A[i, j, k - 1]
            - case_2 = A[i, k, k - 1] + A[k, j, k - 1]
            - A[i, j, k] = min(case_1, case_2)

- Correctness: from optimal substructure + induction, as usual
- Running Time: O(1) per sub-problem, O(n^3) overall 

- What if input graph G has a negative cycle?
    - Answer: will have A[i, i, n] < 0 for at least one i in V at the end of 
      algorithm.
- How to reconstruct a shortest i-j path?
    - Answer: in addition to A, have Floyd-Warshall compute B[i, j] = max label of an internal node on a shortest i-j path for all i, j in V
    - reset B[i, j] = k if 2nd case of recurrence used to compute A[i, j, k]
    - Can use the B[i, j]'s to recursively construct shortest path:
        - source = 23, destination = 17, max_label = 43 -> shortest path 23 
          to 43, 43 to 17 
        - continue until termination

# Johnson's Algorithm

- Recall: APSP reduces to n invocations of SSSP (Suitable Sub-routine for 
  Single Source Problem).
    - non-negative edge length: O(m * n log n) via Dijkstra
    - general edge lengths: O(m * n^2) via Bellman-Ford

- Johnson's Algorithm:
    - 1 invocation of Bellman-Ford (O(m * n))
    - n invocations of Dijksta's (O(n * m * log n))
     
A Re~~~~-weighting Technique - 8:48
