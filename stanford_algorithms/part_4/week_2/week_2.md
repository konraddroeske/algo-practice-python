### NP-Completeness

- Focus of this course (+ Part 1): practical algorithms + supporting theory
  for fundamental computational problems.
- Sad fact: many important problems seem impossible to solve efficiently.

- Next: How to formalize computational intractability using NP-completeness.
- Later: Algorithmic approaches to NP-complete problems.

### Polynomial-Time Solvability

- Question: how to formalize (in)tractability?
- Definition: a problem is polynomial-time solvable if there is an algorithm
  that correctly solves it in O(n^k) time, for some constant k.
	- where n = input length = # of keystrokes needed to describe input
	- yes, even k = 10000 is sufficient for this definition

- Comment: will focus on deterministic algorithms, but to first order
  doesn't matter.

### The Class P

- Definition: P = the set of poly-time solvable problems
- Examples:
	- everything we've seen in this course except:
		- cycle-free shortest paths in graphs with negative cycles
		- knapsack problem
			- running time of our algorithm was O(n * w)
			- but input length proportional to log W
- Interpretation: rough litmus test for "computational tractability"

### Traveling Salesman Problem

- Input: complete undirected graph with non-negative edge costs
- Output: a min-cost tour [i.e., a cycle that visits every vertex exactly once]
- Conjecture: there is no polynomial-time algorithm for TSP.
	- as we'll see, equivalent to P != NP

- Really good idea: amass evidence of intractability via "relative"
  difficulty - TSP "as hard as" lots of other problems.

- Definition: [a little informal] problem Pi, reduces to problem Pi_2 if:
  given a polynomial-time subroutine for Pi_2, can use it to solve Pi, in
  polynomial time.

### Completeness

- Suppose Pi_1, reduces to Pi_2
- Contrapositive: if Pi_1 is not in P, then neither is Pi_2
- That is: Pi_2 is at least as hard as Pi_1
- Definition:
	- Let C = a set of problems
	- the problem Pi is C-complete if:
		- Pi is a member of C
		- everything in C reduces to Pi (at least as hard as everything in C)
	- That is: Pi is the hardest problem in all of C

- Choice of the Class C
	- Idea: show TSP (traveling sales problem) is C-complete for a REALLY
	  BIG set C.
	- How about: show this where C = ALL problems
	- Halting Problem:
		- given a program and an input for it, will it eventually halt?
	- Fact: no algorithm, however slow, guaranteed to solve the Halting Problem.
	- Contrast: TSP definitely solvable in finite time (via brute-force search).
	- Refined idea: TSP as hard as all brute-force-solvable problems.

### The Class NP

- Refined idea: Prove that TSP is as hard as all brute-force-solvable problems.

- Definition: a problem is in NP if:
	1. solutions always have length polynomial in the input size
	2. purported solutions can be verified in polynomial time

- Examples:
	- is there a TSP tour with length <= 1000?
	- constraint satisfaction problem (e.g., 3 SAT)

- Note: every problem in NP can be solved by brute-force search in
  exponential time.
	- just check every candidate solution

- Fact: vast majority of natural computational problems are in NP
	- can recognize a solution

- By definition of completeness:
	- a polynomial-time algorithm for one NP-complete problem solves
	  ***every*** problem in NP efficiently
		- i.e., implies that P = NP

- Interpretation: an NP-complete problem encodes simultaneously all problems
  for which a solution can be efficiently recognized (a "universal" problem).
- Question: Can such problems really exist?
	- NP-complete problems exist
	- 1000s of natural and important problems are NP-complete (including TSP)

- The following recipe for proving that a problem Pi is NP-complete:
	1. find a known NP-complete problem Pi'
	2. prove that Pi' reduces to Pi
		- implies that Pi at least as hard at Pi'
		- Pi is NP-complete as well (assuming Pi is an NP problem)

### The P vs. NP Question

- Question: Is P = NP?
	- P -> polynomial-time solvable
	- NP -> can verify correctness of a solution in polynomial time?
- Widely conjectured: P != NP
- But: has ***not*** been proved
- Reasons to believe:
	- (psychological) if P = NP, someone would have proved it by now
	- (philosophical) if P = NP, then finding a proof always as easy as
	  verifying one
	- (mathematical) ??

- FAQ: What does "NP" stand for?
	- "Non-deterministic polynomial"
	- modern, mathematically equivalent definition via efficient
	  verification of purported solutions
- Passed over: PET
	- "possibly exponential time"
	- if P != NP, "provably exponential time"
	- if P = NP, "previously exponential time"

- Question: so your problem is NP-complete. Now what?
- Important: NP-completeness is not a death sentence.
	- but, need appropriate expectations / strategy

- Three useful strategies:
	1. Focus on computationally tractable special cases
		- Examples:
			- WIS (weighted independent set) in path graphs (and trees,
			  bounded tree width)
			- Knapsack with polynomial size capacity (e.g., w = O(n))
			- 2 SAT (P) instead of 3 SAT (NP-C)
			- vertex cover problem when OPT is small
	2. Heuristics
		- Fast algorithms that are not always correct
		- Examples:
			- greedy and dynamic programming-based heuristics for knapsack.
	3. Solve in exponential time but faster than brute-force search
		- knapsack (O(n*w) instead of 2^n)
		- TSP (2^n instead of n!)
		- Vertex Cover (2^(OPT)*n instead of n^(OPT))

### Vertex Cover Problem

- Input: an undirected graph G = (V, E)
- Goal:
	- compute a minimum-cardinality vertex cover - a subset S in V that
	  contains at least one endpoint of each edge of G

- Strategies for NP-Complete problems:
	1. identify computationally tractable special cases
		- trees (application of dynamic programming)
		- bipartite graphs (application of maximum flow problem)
		- when the optimal solution is small (log n or less)
	2. heuristics (e.g., via greedy algorithms)
	3. exponential-time but better than brute-force search

- Given: an undirected graph G = (V, E)
- Goal: compute a minimum-cardinality vertex cover (a set S in E that
  includes at least one endpoint of each edge of E)
- Suppose: given a positive integer k as input, we want to check whether
  there is a vertex cover with size <= k.
	- think of k as "small"
- Note: could try all possibilities, would take O(n^k) time
- Question: Can we do better?

- Substructure Lemma: Consider the graph G, edge (u, v) in G, integer k >= 1
- Let G_u = G with u and its incident edges deleted (similarly, G_v)
- Then, G has a vertex cover of size k IFF G_u or G_v (or both) have vertex
  covers of size (k - 1)
- Left:
	- Suppose G_u has a vertex cover of size (k - 1)
	- E = E_u (inside G_u) U F_u (incident to u)
	- Since S has an endpoint of each edge of E_u, S U {u} is a vertex cover
	  (of size k) of G
- Right:
	- Let S = a vertex cover of G of size k.
	- Since (u, v) an edge of G, at least one u, v (say u) is in S
	- Since no edges of E_u incident on u, S - {u} must be a vertex cover of
	  size (k - 1) of G_u

### A search algorithm

- given an undirected graph G = (V, E), integer k
- ignore base cases

1. Pick an arbitrary edge (u, v) in E
2. Recursively search for a vertex cover S of size (k - 1) in G_u. If found,
   return S U {u}
	- G with u + its incident edges deleted
3. Recursively search for a vertex cover S of size (k - 1) in G_v. If found,
   return S U {v}

- Correctness: straightforward induction, using the substructure lemma to
  justify the inductive step
- Running time: Total number of recursive calls is O(2^k)
	- formally, proof by induction on k
	- branching factor <= 2, recursion depth <= k
	- also, O(m) work per recursive call (not counting work done by recursive
	  sub-calls)
	- running time = O(2^k * m)
		- way better than O(n^k)
		- polynomial-time as long as k = O(log n)
		- remains feasible even when k = 20

### The Traveling Salesman Problem

- Input: a complete undirected graph with non-negative edge costs
- Output: a minimum-cost tour (i.e., a cycle that visits every vertex
  exactly once)
- Brute-Force search: takes ~= n! time
	- tractable only for n ~= 12, 13
- Dynamic Programming: will obtain O(n^2 * 2^n) running time
	- tractable only for n ~= 30

- Optimal Substructure Lemma
	- Idea: copy the format of the Bellman-Ford algorithm
	- Proposed sub-problems: for every edge budget i in {0, 1, 2, ..., n},
	  destination j in {1, 2, ..., n}, let:
		- L_ij = length of a shortest path form 1 to j that uses exactly i 
		  edges and no repeated vertices
 
- Hope: use the following recurrence
	- L_ij = min (k != 1, j) { L_i-1,k + c_kj }
		- shortest path from 1 to k, (i - 1) edges, no repeated vertices
        - cost of final hop

- Problem: what if j already appears on the shortest 1 -> k path with (i - 1)
  edges and no repeated vertices?
	- concatenating (k, j) yields a second visit to j (not allowed)

The Traveling Salesman Problem - 13:56
