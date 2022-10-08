### Motivations

1. Check if a network is connected (can get to anywhere from anywhere else)
2. Driving directions
3. Formulate a plan [e.g, how to fill in a Sudoku puzzle]
    - nodes = a partially completed puzzle
    - arcs = filling in one new square
4. Compute the "pieces" (or "components") of a graph
    - clustering, structure of the web graph, etc.

### Generic Graph Search

Goals:

1. Find everything findable from a given start vertex
2. Don't explore anything twice

Time Complexity Goal: O(m + n) - m edges, n nodes

### Generic Algorithm (given graph G, vertex s)

- initially s explored, all other vertices unexplored
- while possible:
    - choose an edge (u, v) with u explored and v unexplored (if none, halt)
    - mark v explored

Claim: at the end of the algorithm, v explored <==> G has a path from s to v
(G undirected or directed)

### BFS vs DFS

Note: How to choose among the possibly many "frontier" edges?

### Breadth-First Search (BFS)

- Explore nodes in "layers"
- Can compute the shortest path
- Can compute connected components of an undirected graph
- Complexity: O(m + n) using a queue (FIFO)

### Depth-First Search (DFS)

- Explore aggressively like a maze, backtrack only when necessary
- Compute topological ordering of directed acyclic graph
- Compute connected components in directed graphs
- Complexity: O(m + n) using a stack (LIFO) (or via recursion)

### Breadth First Search Implementation

BFS (graph G, start vertex S)

- all nodes initially unexplored
- mark s as explored
- let Q = queue data structure (FIFO), initialized with s

- while Q is not empty:
    - remove the first node of Q, call it v
    - for each edge (v, w):
        - if w unexplored:
            - mark w as explored
            - add into Q (at the end)

Claim #1: at the end of BFS, v explored <==> G has a path from s to v.

Claim #2: running of main while loop = O(n_s + m_s), where:

- n_s = # of nodes that can be reached from s
- m_s = # of edges that can be reached from s

### BFS and Shortest Path

Goal: Compute dist(v), the fewest # of edges on a path from s to v.

Extra code:

- initialize dist(v) = {0 if v = s, +infinity if v != s}
- when considering edge (v, w):
    - if w unexplored, then set dist(w) = dist(v) + 1

Claim: at termination, dist(v) = i <==> v in ith layer (i.e, <==> shortest s-v path has i edges).

Proof Idea: every layer-i node w is added to Q by a layer-(i-1) node v via the edge (v, w).

### BFS and Undirected Connectivity

Let G = (V, E) be an undirected graph

Connected components = the "pieces" of G

- Formal definition:
    - Equivalence classes of the relation u~v <==> there exists u-v path in G.

- Goal: Compute all connected components.

- Why?:
    - Check if network is disconnected.
    - Graph visualization
    - Clustering

- To compute all components (undirected case):
    - all nodes unexplored (assume labelled 1 to n) -> O(n)
    - for i = 1 to n -> O(n)
        - if i not yet explored (in some previous BFS) -> O(n)
            - BFS (G, i) -> discovers precisely i's connected component

Note: finds every connected component

Running Time: O(m + n) -> O(1) per node, O(1) per edge in each BFS

### Depth-First Search (DFS): The Basics

- Explore aggressively, only backtrack when necessary.
- Also computes a topological ordering of a directed acyclic graph
- And strongly connected components of directed graphs

RunTime: O(m + n)

Exercise: mimic BFS code, use a stack instead of a queue (+ minor other modifications).

- Recursive version:
    - DFS (graph G, start vertex s):
        - mark s as explored
        - for every edge (s, v):
            - if v unexplored
                - DFS (G, v)

- Claim #1:
    - at end of the algorithm, v marked as explored <==> there exists path from s to v in G
    - Reason: particular instantiation of generic search procedure.

- Claim #2:
    - Running time is O(n_s + m_s)
        - n_s: number of nodes reachable from s
        - m_s: number of edges reachable from s
    - Reason: look at each node in connected component of s at most once, each edge at most twice

### Topological Sort

- Definition:
    - A topological ordering of a directed graph G is a labelling f of G's nodes such that:
        - the f(v)'s are the set {1, 2, ..., n}
        - (u, v) E G => f(u) < f(v)

- Motivation:
    - Sequence tasks while respecting all precedence constraints.

- Note: G has directed cycle => no topological ordering

Straightforward Solution:

- Note: Every directed acyclic graph has a sink vertex.
- Reason: if not, can keep following outgoing arcs to produce a directed cycle.
- To compute topological ordering:
    - let v be a sink vertex of G
    - set f(v) = n
    - recurse on G-{v}

- Why does it work?
    - when v is assigned to the position i, all outgoing arcs are already deleted
        - => all lead to later vertices in ordering

Slick Solution:

- DFS-Loop (graph G)
    - mark all nodes unexplored
    - current_label = n (to keep track of ordering)
    - for each vertex v E G:
        - if v not explored yet (in some previous DFS call)
            - DFS(G, v)

- DFS (graph G, start vertex S)
    - mark s explored
    - for every edge (s, v):
        - if v not yet explored
            - DFS(G, v)
    - set F(s) = current_label
    - current_label-- (decrement)

- Running Time: O(m + n),
    - only constant time for each node,
    - only visit each edge once

Correctness: need to show that if (u, v) is an edge, then f(u) < f(v)

- Case 1: u visited by DFS before v.
    - Recursive call corresponding to v finishes before that of u (since DFS)
- Case 2: v visited before u.
    - v's recursive call finishes before u's even starts.
    - f(v) > f(u)

### Computing Strong Components: The Algorithm

***Strongly Connected Components***

Formal Definition:

The strongly connected components (SCCs) of a directed graph G are the equivalence classes of the
relation:
u~v <==> there exists path u -> v and a path v -> u in G

***Kosaraju's Two-Pass Algorithm***

Theorem: Can compute in SCCs in O(m + n) time.

Algorithm: (given graph G)

1. Let G_rev = G with all arcs reversed
2. run DFS-Loop on G_rev (goal: compute "magical ordering" of nodes)
    - Let f(v) = "finishing time" of each v E V
3. run DFS-Loop on G (goal: discover the SCCs one-by-one)
    - Processing nodes in decreasing order of finishing times.
    - SCCs = nodes with the same "leader"

DFS-Loop (graph G)

- global variable t = 0 (for finishing times in 1st pass)
    - # of nodes processed so far
- global variable s = NULL (for leaders in 2nd pass)
    - current source vertex
- Assume nodes labelled 1 to n.

- For i = n down to 1:
    - if i not yet explored:
        - s := i
        - DFS(G, i)

- DFS(graph G, node i)
    - mark i as explored (for rest of DFS-Loop)

    - on 2nd pass
        - set leader(i) := s

    - for each arc (i, j) E G:
        - if j not yet explored
            - DFS(G, j)

    - on 1st pass
        - t++
        - set f(i) := t (i's finishing time)

Running Time: 2 * DFS = O(m + n)

***Proof of Kosaraju's Two-Pass Algorithm***

Claim: the SCCs of the directed graph G, induce an acyclic "meta-graph":

- meta-nodes = the SCCs c_1, ..., c_k of G
- There exists arc c -> c_hat <==> There exists arc (i, j) in G with i in c, j in c_hat

Why acyclic?: a cycle of SCCs would collapse into one

- Lemma:
    - Consider two "adjacent" SCCs in G.
    - Let f(v) = finishing times of DFS-Loop in G_rev
    - Then, max v E c_1 f(v) < max v E c_2 f(v)

- Corollary:
    - maximum f-value of G must lie in a "sink SCC".

- By Corollary:
    - 2nd pass of DFS-Loop begins somewhere in a sink SCC C*.
    - first call to DFS discovers C* and nothing else!
    - rest of DFS-Loop like recursing on G with C* deleted
        - starts in a sink node of G-C*
    - successive calls to DFS "peel off" the SCCs one by one
        - in reverse topological order of the "meta graph" of SCCs

### Structure of the Web

- vertices = web pages
- (directed) edges = hyperlinks

- Question: what does the web graph look like?
    - Assume you've already "crawled" it
- Size (year 2000): 200 million nodes, 1 billion edges

- Computed the SCCs of the web graph. (pre Map-Reduce/Hadoop)

***The Bow Tie***

IN -> ( CORE ) -> OUT

- Giant SCC
- In
    - To Giant SCC, but not back
        - i.e. New web pages
- Out
    - From Giant SCC, but not back
        - i.e. Corporate sites
- Residuals:
    - "tubes" from In to Out part, but not back
    - "tendrils" out of In/into Out
    - "islands" of isolated pockets

1. All 4 parts (Giant SCC, In, Out, Residuals tubes/tendrils/islands) are roughly the same size
2. Within Core, is very well-connected (has the "small world" property)
3. Outside Core, surprisingly poor connectivity
