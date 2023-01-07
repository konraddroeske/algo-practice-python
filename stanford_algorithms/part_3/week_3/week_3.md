### Binary Codes

- Binary Code: maps each character of an alphabet (Sigma) to a binary string.
- Example: Sigma = a - z & various punctuation (size 32 overall)
- Obvious encoding: use the 32 5-bit binary string to encode this Sigma (a 
  fixed length code)
- Can we do better?:
    - Yes, if some characters of Sigma are much more frequent than others, 
      using a variable-length code.
    
- Example:
    - Suppose Sigma = [A, B, C, D]
    - Fixed-length encoding = [00, 01, 10, 11]
    - Supposed instead we use the encoding [0, 01, 10, 1] 
        - Problem: Unclear where one symbol starts, and the other begins

- Problem: with variable-length codes, not clear where one character ends + 
  the next one begins
- Solution: prefix-free codes - make sure that for every pair i, j in Sigma, 
  neither of the encodings f(i), f(j) is a prefix of the other.
- Example: 
    - [0, 10, 110, 111] 
    - Take advantage of non-uniform frequency.


## Huffman Codes

### Codes as Trees

- Goal: the best binary prefix-free encoding for a given set of character 
  frequencies.
- Useful fact: binary codes <--> binary trees
 
- In general: 
  - left child edges <--> "0", right child edges <--> "1"
  - for each i in Sigma, exactly one node labeled "i"
  - encoding of i in Sigma <--> bits along path from root to the node "i"
  - prefix-free <--> labelled nodes = the leaves
    - since prefixes <--> one node an ancestor of another

- To decode:
  - repeatedly follow path from root until you hit a leaf.
   
- Note: encoding length of i in Sigma = depth of i in tree

### Problem Definition

- Input: probability p_i for each character i in Sigma
- Notation: if T = tree with leaves <--> symbols of Sigma, then average 
  encoding length is: 
  - L(T) = Sum (i in Sigma) p_i * [depth of i in T]
- Output: a binary tree T minimizing the average encoding length L.

- Question: what's a principled approach for building a tree with leaves 
  <--> symbol of Sigma?
- Natural, but suboptimal: top-down/divide + conquer
  - partition Sigma into S_1, S_2 each with ~= 50% of total frequency
  - recursively compute T_1 for S_1, T_2 for S_2, return 
- Huffman's (optimal) idea:
  - build tree bottom-up using successive mergers.

### A Greedy Approach

- Question: Which pair of symbols is "safe" to merge?
- Observation: final encoding length of i in Sigma = # of mergers its 
  subtree endures

### How to recurse? 

- Suppose: 1st iteration of algorithm merges symbols a & b
- Idea: replace the symbols a, b by a new "meta-symbol" ab
- Huffman's Algorithm:
  - If | Sigma | = 2, return A -0- ( ) -1- B 
   
  - let a, b in Sigma have the smallest frequencies
  - let Sigma' = Sigma with a, b replaced by new symbol ab
  - Define p_ab = p_a + p_b
  - Recursively compute T' (for the alphabet Sigma')
  
  - Extend T' (w/ leaves <--> Sigma') to a tree T with leaves <--> Sigma by 
    splitting leaf ab into two leaves a & b
  - Return T

### A More Complex Example 

- Input:
  - characters: A, B, C, D, E, F
  - weights: 3, 2, 6, 8, 2, 6
- Step 1:
  - merge B & E
  - A BE C D F
  - 3 4  6 8 6
- Step 2:
  - merge A & BE
  - ABE C D F
  - 7   6 8 6
- Step 3:
  - merge C & F
  - ABE D CF
  - 7   8 12
- Step 4:
  - ABED CF
  - 15   12
- Step 5:
  - ABEDCF
  - 27

- Corresponding code:
  - A: 000
  - B: 0010
  - C: 10
  - D: 01
  - E: 0011
  - F: 11

### Correctness Proof

- Theorem: Huffman's algorithm computes a binary tree (with leaves <--> 
  symbol of Sigma) that minimizes the average encoding length.

L(T) = Sum (i in Sigma) p_i * [depth of leaf i in T]

- Proof: by induction on n = | Sigma | (can assume n >= 2)
- Base case: when n = 2, algorithm outputs the optimal tree
  - Need 1 bit per symbol
- Inductive step: fix input with n = | Sigma | > 2
- By Inductive hypothesis: algorithm solves smaller sub-problem (for Sigma') 
  optimally.

- Let Sigma' = Sigma with a, b replace by meta-symbol ab.
- Define p_ab = p_a + p_b
- Recall: exact correspondence between trees for Sigma' <--> trees for Sigma 
  that have a, b as siblings (X_ab)
- Important: for every such pair T' and T, L(T) - L(T') is (after cancellation):
  - p_a * [depth of a in T] + p_b * [depth of b in T] - p_ab * [depth of ab 
    in T']
  - p_a * (d + 1) + p_b * (d + 1) - (p_a + p_b) * d
  - p_a + p_b (independent of T, T')
 
- Inductive Hypothesis: Huffman's algorithm computes a tree T_hat' that 
  minimizes L(T') for Sigma'.
- Upshot: corresponding tree T_hat minimizes L(T) for Sigma over all trees 
  in X_ab (i.e. where a & b are siblings)
- Key lemma: there is an optimal tree (for Sigma) in X_ab.
  - i.e., a & b were "safe" to merge
- Intuition: can make an optimal tree better by pushing a & b as deep as 
  possible (since a, b have smaller frequencies)

### Proof of Key Lemma

- By exchange argument: Let T* be any tree that minimizes L(T) for Sigma.
- Let x, y be siblings at the deepest level of T*
- The exchange: object T_hat from T* by:
  - swapping labels a <--> x, b <--> y
- Note: T_hat in X_ab (by choice of x, y)
- To Finish: will show that L(T_hat) <= L(T*)
  - T_hat also optimal, completes proof
- Reason: 
  - L(T*) - L(T_hat) = (p_x - p_a) * [depth of x in T* - depth of a in T*] + 
    (p_y - p_b) * [depth of y in T* - depth of b in T*] >= 0

### Notes on Running Time

- Naive Implementation: O(n^2) time, where n = | Sigma |
 
- Speed-ups: use a heap! [to perform repeated minimum computations]
- use keys = frequencies
- after extracting the two smallest-frequency symbols, re-insert the new 
  meta-symbol [new key = sum of the 2 old ones]
- iterative, O (n log n) implementation
 
- Even Faster: (non-trivial exercise) Sorting + O(n) additional work.
  - manage (meta-)symbols using two queues


## Dynamic Programming

### Weighted Independent Set Problem (WIS)

- Input: a path graph G = (V, E) with non-negative weights on vertices.
- Desired output: subset of non-adjacent vertices - an independent set - of 
  maximum total weight.
- Next: iterate through our algorithm design principles.

- Greedy: iteratively choose the max-weight vertex not adjacent to any 
  previously chosen vertex.

- Divide & Conquer: recursively compute the max-weight independent set of 
  1st half, 2nd half, then combine.
   - What if recursive sub-solutions conflict? Not clear how to fix.

- Critical Step: reason about structure of an optimal solution [in terms of 
  optimal solutions of smaller subproblems]
- Motivation: this thought experiment narrows down the set of candidates for 
  the optimal solution; can search through the small set using brute-force 
  search.
- Notation: Let S <ins>c</ins> V be a max-weight independent set (IS).
  - Let v_n = last vertex of path
  
- Case 1: suppose v_n not in S. Let G' = G with v_n deleted.
- Note: S also an IS of G' 
- Note: S must be a max-weight IS of G' - if S* was better, it would also be 
  better than S in G. [contradiction]

- Case 2: suppose v_n in S
- Note: previous vertex v_(n-1) not in S. Let G'' = G with v_(n-1), v_n 
  deleted [by definition of an IS]
- Note: S - {v_n} is an IS of G''
- Note: must in fact be a max-weight IS of G'' - if S* is better than S in 
  G'', then S* U {v_n} is better than S in G [contradiction]

- Upshot: a max-weight IS must be either:
  (i) a max-weight IS of G'
  (ii) v_n + a max-weight IS of G''
- Corollary: if we knew whether v_n was in the max-weight IS, could 
  recursively compute the max-weight IS of G' or G'' and be done.
- (Crazy?) idea: try both possibilities and return the better solution. 

### Linear Time Algorithm

- Upshot: if we knew whether v_n is in the max-weight IS, then we 
  could recursively compute the max-weight IS of G' or G'' and be done.
- Proposed algorithm: 
  - recursively compute s_1 = max-weight IS of G'
  - recursively compute s_2 = max-weight IS of G''
  - return s_1 or s_2 U {v_n}, whichever is better
- Good news: Correct.
- Bad news: exponential time.

### Eliminating Redundancy

- Obvious fix: the first time you solve a sub-problem, cache its solution in 
  a global table for O(1)-time lookup later on. ["memoization"]
 
- Even better: reformulate as a bottom-up iterative algorithm.
  - Let G_i = 1st i vertices of G
- Plan: populate array A left to right with A[i] = value of max-weight IS of G_i
- Initialization: A[0] = 0, A[1] = w_1
- Main loop:
  - For i = 2, 3, 4, ..., n:
    - A[i] = max {A[i - 1], A[i - 2] + w_i}
- Runtime: O(n)
- Correctness: same as recursive version

### Optimal Value vs Optimal Solution

- Recall: A[0] = O, A[1] = w_1, for i = 2, 3, 4, to n: A[i] := max {A[i - 1],
  A[i - 2] + w_i}
- Note: algorithm computes the value of a max-weight IS, not such an IS itself.
- Correct, but not ideal: store optimal IS of each G_i in an array in 
  addition to its value.
- Better: trace back through filled-in array to reconstruct optimal solution.
- Key point:
  - we know that a vertex v_i belongs to a max-weight IS of G_i
  - w_i + max-weight IS of G_(i-2) >= max-weight IS of G_(i-1)

### A Reconstruction Algorithm

- Let A = filled-in array A
- Let S != None
- while i >= 1: [scan through array from right to left]
  - if A[i - 1] >= A[i - 2] + w_i [i.e., Case 1 wins]
    - decrease i by 1
  - else [i.e., Case 2 wins]
    - add w_i to S, decrease i by 2
- return S

- Claim: by induction + our case analysis, final output S is a max-weight IS 
  of G
- Running time: O(n)

### Principle of Dynamic Programming

- Key ingredients of DP:
  1. Identify a small number of sub-problems
    - e.g. compute the max-weight IS of G_i, for i = 0, 1, 2, 3, ..., n 
  2. Can quick + correctly solve "larger" sub-problems given the solutions 
     to "smaller sub-problems"
    - Usually via a recurrence such as A[i] = max {A[i - 1], A[i - 2] + w_i}
  3. After solving all sub-problems, can quickly compute the final solution.
    - usually, it's just the answer to the "biggest" sub-problem
