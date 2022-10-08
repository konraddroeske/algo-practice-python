### Graphs

- 2 Ingredients:
    - vertices aka nodes (V)
    - edges (e) = pairs of vertices
        - can be undirected (unordered)
        - or directed (ordered pair), aka arcs


- Reasons to use:
    - Road networks (vertices are intersections, edges are roads)
    - The web (vertices are webpages, edges are hyperlinks)
    - Social networks

- Definitions:
    - A **cut** of a graph (V, E) is a partition of V into two non-empty sets A and B
    - The **crossing edges** of a cut (A, B) are those that satisfy:
        - One endpoint in each (A, B) (undirected)
        - Tail in A, Head in B (directed)
    - **Parallel edges** two edges which correspond to 2 vertices.

- Graph Partitioning:
    - Identifying network bottlenecks/weaknesses.
    - Community detection.
    - Image segmentation
        - input = graph of pixels
        - use edge weights (how likely do you expected pixels to come from a common object)

- Sparse vs Dense Graphs
    - Let n = # of vertices, m = # of edges
    - In most (but not all) applications, m is Omega(n) and O(n^2)
    - In a **sparse graph**, m is O(n) or close to it
    - In a **dense graph**, m is closer to O(n^2)

- Adjacency Matrix:
    - Represent the edges in a graph using a matrix
    - n x n 0-1 matrix A, where A_ij = 1 has an i-j edge
    - Variants:
        - A_ij = # of i-j edges (if parallel edges)
        - A_ij = weight of i-j edge (if any)
        - A_ij = { +1 if i -> j, -1 if i <- j }
    - Space Requirements:
        - O(n^2), good for dense graph, wasteful if sparse graph

- Adjacency List:
    - Ingredients:
        - array of vertices (O(n))
        - array of edges (O(m))
        - each edge points to its endpoints (O(m))
        - each vertex points to edges incident on it (O(m))
    - Space Requirements:
        - O(3m + n) -> O(m + n)
        - or O(max {m, n})

- Which to use?
    - It depends on graph density and operations needed.

### Random Contract Algorithm

- Input: an undirected graph, G = (V, E)
    - Parallel edges allowed

- Goal: Compute a cut with the fewest number of crossing edges. (a min cut)

- While there are more than 2 vertices:
    - Pick a remaining edge (u, v) uniformly at random
    - Merge (or "contract") u and v into a single vertex
    - Remove self-loops

Return cut represented by the final 2 vertices.

- Question: What is the probability of success?

Fix a graph G = (V, E) with n vertices, m edges.
Fix a minimum cut (A, B).

Let k = # of edges crossing (A, B). (Call those edges F)

Outcomes:

- If one of the edges of F gets chosen for contraction -> algorithm will not output (A, B)
- Suppose only edges inside A or inside B get contracted -> algorithm will output (A, B)

Thus: Pr[output is (A, B)] = Pr[never contracts an edge of F]

Let S_i = event that an edge of F contracted in iteration i.

### First Iteration:

Pr[S_1] = # of crossing edges / # of edges = k / m

Key Observation: degree (# of edges) of each vertex (n) is at least k.

Reason: each vertex v defines a cut ({v}, V - {v})

Since Sum(v) degree(v) = 2m, we have: m >= (k * n) / 2

Since Pr[S_1] = k / m, Pr[S_1] <= k * (2 / k * n)
-> Pr[S_1] <= 2 / n

### Second Iteration:

Recall: Pr[not S_1 intersects not S_2] = Pr[not S_2 | not S_1] * Pr[not S_1]
= (1 - (k / # of remaining edges)) * (1 - (2 / n))

Note: all nodes in contracted graph define cuts in G (with at least k crossing edges)
-> all degrees in contracted graph are at least k

So: # of remaining edges >= 1/2 * k * (n - 1)

Pr[not S_2 | not S_1] >= 1 - (2 / (n - 1))

### In general:

Pr[not S_1 intersects not S_2, ..., not S_n-2] 
= Pr[not S_1] * Pr[not S_2 | not S_1] * Pr[not S_3 | not S_1 intersects not S_2] * ... * Pr[not S_n-2 | not S_1 intersects ... not S_n-3]
>= (1 - 2/n) * (1 - 2/n-1) * (1 - 2/n-2) ... (1 - 2/n-(n-4))(1 - 3/n-(n-3))
= (n - 2 / n) * (n - 3 / n - 1) * (n - 4 / n - 2) * ... * 2/4 * 1/3
= 2 / n*(n - 1) 
>= 1 / n^2

Probability not great, what is the solution?
- Run the algorithm a large number N times, remember the smallest cut found.

How many trials needed?
- Let T_i = event that the cut (A, B)  is found on the ith try.
- by definition, different T_i's are independent

So: Pr[all N trials fail] = Pr[not T_1 intersects not T_2 ... intersects not T_N]
= Sum(N, i = 1) Pr[not T_i] <= (1 - 1/(n^2))^N

Calculus Fact: For all real numbers x, 1 + x <= e ^ x

So: if we take N = n^2, Pr[all fail] <= (e ^ (-1/(n^2)))^(n^2) = 1 / e

If we take N = n^2 * ln n, Pr[all fail] <= (1/e)^(ln n) = 1 / n

Running Time: polynomial in n and m but slow (Omega (n^2 * m))
But, can get big speedups (to roughly O(n^2))

### The Number of Minimum Cuts

Note: a graph can have multiple min cuts. (e.g. a tree with n vertices has (n-1) min cuts)

Question: what's the largest number of min cuts that a graph with n vertices have?

Answer:(n 2) = n (n - 1) / 2

- The Lower Bound:
    - Consider the n-cycle.
    - Each pair of the n edges defines a distinct min cut (with two crossing edges).

- The Upper Bound:
    - Let (A_1, B_1) , (A_2, B_2), ..., (A_t, B_t) be the min cuts of a graph with n verticies.
    - By the Contraction Algorithm analysis (without repeated trials):
        - For each t cut, the probability that algorithm outputs A_i, B_i is:
        - Pr[Output = (A_i, B_i)]  >= 2/(n * (n - 1)) = 1/(n 2) for all i = 1, 2, ..., t
