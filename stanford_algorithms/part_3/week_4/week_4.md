### The Knapsack Problem

- Input: n items. Each has a value:
    - value v_i (non-negative)
    - size w_i (non-negative and integer)
    - capacity W (a non-negative integer)
- Output: a subset S <u>C</u> {1, 2, 3, ..., n}
    - That maximizes sum v_i subject to sum w_i <= W


### Developing a Dynamic Programming Algorithm

- Step 1: Formulate Recurrence [optimal solution as a function of solutions 
  to "smaller" sub-problems] based on structure of an optimal solution.
    - Let S = a max-value solution to an instance of knapsack
    - Case 1: suppose item n not in S.
      - S must be optimal with the first (n - 1) items (same capacity W)
      - If S* were better than S with response to 1st (n - 1) items, then 
        this equally true wrt all n items - contradiction

    - Case 2: suppose item n in S. Then S - [n] is an optimal solution wrt 
      the 1st (n - 1) items and capacity W - w_n
      - Proof: if S* has higher value than S - [n] and total size <= W - w_n, 
        then S* with [n] has size <= W and value more than S [contradiction]

- Notation: let V_i,x = value of the best solution on that:
    1. uses only the first i items
    2. has total size <= x

- Upshot of the last video: for i in {1, 2, ..., n} and only x,

v_i_x = max {
    v_(i-1)_x, -> case 1, item i excluded
    v_i + v_(i-1)_(x-w_i) -> case 2, item i included
}

- Edge case: if w_i > x, must have v_i_x = v_(i-1)_x

- Step 2: Identify Sub-Problems 
    - all possible prefixes of items {1, 2, ..., i}
    - all possible (integral) residual capacities of x in {0, 1, 2, ..., W}
        - recall W and the w_i's are integral

- Step 3: Use recurrence from Step 1 to systematically solve all sub-problems.

Let A = 2-D Array.

Initialize A[0, x] = 0 for x = 0, 1, 2, ..., W

- for i = 1, 2, ..., n: (items)
    - for x = 0, 1, ..., W: (capacities)
        - if w_i > x: 
            - A[i, x] := A[i - 1, x]
        - else: 
            - A[i, x] := max {A[i - 1, x], A[i - 1, x - w_i] + v_i}
            - Both options have been previous computed for O(1) look-up

return A[n, W]

- Running time: O(n * W)
- Correctness: straightforward induction [use Step 1 argument to justify 
  inductive step].

- Reconstruction Algorithm - TBD

### Concrete Example

n = 4, W = 6

- Initialization:
    - A[0, x] = 0 for all x
- Main loop:
    - for i = 1 to n
        - for x = 0 to w
            - A[i, x] := max {A[i - 1, x], A[i - 1, x - w_i] + v_i}

W = 6
v_1 = 3, w_1 = 4
v_2 = 2, w_2 = 3
v_3 = 4, w_3 = 2
v_4 = 4, w_4 = 3 

### Sequence Alignment Problem

- Recall: sequence alignment [Needleman-Wunsch Score = Similarity measure 
  b/w string]
- Example: 
    - AGGGCT
    - AGG-CA
    - Total penalty: x_gap + x_mismatch
- Input: strings X = x_i, ..., x_m, Y = y_i, ..., y_n over some alphabet 
  (like A, C, G, T)
- Penalty p_gap >= 0 for inserting a gap, p_ab for matching a & b 
  [presumably p_ab = 0 if a = b]
- Feasible solutions:
    -  alignments - i.e. insert gaps to equalize length of the strings
- Goal: compute the alignment that minimized penalty.

- Key step: identify the sub-problems. As usual, will look at structure of 
  an optimal solution for clues.
    - i.e. develop a recurrence then reverse engineer the sub-problems

- Structure of optimal solution: consider an optimal alignment of X, Y 
    - x + gaps
    - y + gaps
- How many relevant possibilities for final position?
    - Case 1: x_m, y_n matched
    - Case 2: x_m matched with gap
    - Case 3: y_n matched with gap
    - Case 4: not relevant, if both are gap, just remove to avoid penalty

- Point: narrow optimal solution own to 3 candidates.
 
- Optimal substructure: 
    - Let X' = X - x_m, Y' = Y - y_n,
    - If Case 1 holds:
        - then induced alignment of X' and Y' is optimal
    - If Case 2 holds:
        - then induced alignment of X' and Y is optimal
    - If Case 3 holds:
        - then induced alignment of X and Y' is optimal


- Optimal Substructure Proof: [of case 1, other cases are similar]
    - By contradiction. Supposed induced alignment of X', Y' has penalty P 
      while some other one has penalty P* < P
    - Appending x_m and y_n to the latter, get an alignment of X and Y with 
      penalty P* + p_xm_yn < P + p_xm_yn
    - Contradicts optimality of origin alignment of X & Y

- Relevant sub-problems:
    - have the form (x_i, y_j), where:
        - x_i = 1st i letters of X
        - y_j = 1st j letters of Y

- Recurrence:
    - Notation: P_ij = penalty of optimal alignment of x_i and y_j
    - Recurrence:
        - for all i = 1, 2, 3, ..., m and j = 1, 2, 3, ..., m
        - P_ij = 
            - Case 1: p_xi_yj (match) + P_(i-1)_(j-1)
            - Case 2: p_gap + P_(i-1)_j
            - Case 3: p_gap + P_i_(j-1) 
    - Correctness: optimal solution is one of these 3 candidates and 
      recurrence selects the best of these.

A = 2-D Array
A[i, 0] = A[0, i] = i * p_gap, for all i >= 0

- for i = 1 to m:
    - for j = 1 to n:
        - A[i, j] = min
            - A[i-1, j-1] + p_xi_yj
            - A[i-1, j] + p_gap
            - A[i, j-1] + p_gap
            - All available for O(1)-time lookup!
             
- Correctness:
    - i.e., A[i, j] = P_ij for all i, j >= 0

- Running Time: O(m * n)

- Reconstructing a solution:
    - trace back through filled-in table A, starting at A[m, n]
    - when you reach sub-problem A[i, j]:
        - if A[i, j] filled using Case 1, match x_i & y_j and go to A[i - 1, 
          j - 1]
        - if A[i, j] filled using Case 2, match x_i with a gap and go to A
          [i-1, j]
        - if A[i, j] filled with Case 3, match y_j with a gap and go to A[i, 
          j-1]
        - if i = 0 or j = 0, match remaining sub-string with gaps


### Optimal Binary Search Trees

- Recall:
    - Left nodes, keys less than x
    - Right nodes, keys bigger than x
    - For a given set of keys, there are lots of valid search trees.
        - Balanced
        - Chain
- Question: What is the "best" search tree for a given set of keys?
    - A good answer: a balanced search tree, like a red-black tree.
    - worst-case search time= O(height) = O(log n)
     
- Question: suppose we have keys x < y < z and we know that:
    - 80% of searches are for x
    - 10% of searches are for y
    - 10% of searches are for z
    - What is the average search time (i.e. number of nodes looked at) in 
      the trees:
        - x <- y -> z (1.9)
        - x -> y -> z (1.3)

- Input: frequencies p_1, p_2,..., p_n for items 1, 2, ..., n
    - assume items in sorted order, 1 < 2 < 3 < ... < n
- Goal: compute a valid search tree that minimizes the weighted (average) 
  search time.
 
C(T) = sum (items i) p_i * [search time for i in T] <- depth of i in T + 1 

- Example: if T is a red-black tree, then C(T) = O(log n)
    - assuming sum p_i = 1

- Similarities w/ Huffman Codes
    - output = a binary tree
    - goal is (essentially) to minimize average depth with respect to given 
      probabilities
- Differences:
    - with Huffman codes, constraint was prefix-free 
        - symbols only at leaves (not internal nodes)
    - here, constraint = search tree property
        - seems harder to deal with

- Greedy Doesn't Work
    - Intuition: want the most frequently accessed items closest to the root.
- Ideas for greedy algorithms:
    - bottom-up [populate lowerst level with least frequently accessed keys]
    - top-down

- Choosing the root:
    - Issue: with the top-down approach, the choice of root has 
      hard-to-predict repercussions further down the tree.
        - stymies both greedy and divide & conquer approaches 

- Idea: what if we knew the root?
    - i.e., maybe can try all possibilities within a dynamic programming 
      algorithm!

- Proof:
    - Let T be an optimal BST for keys { 1, 2, ..., n } with frequencies p_1,
      ..., p_n. Suppose T has root r.
    - Suppose for contradiction that T_1 is not optimal for { 1, 2, ..., r - 
      1 } with C(T_1*) < C(T_1)
    - Obtain T* from T by "cutting + pasting" T_1* in T_1
    - Note: to complete contradiction + proof, only need to show that C(T*)< 
      C(T)

***Refer to lecture notes for proof.***

- Optimal Substructure Lemma: If T is an optimal BST for the key { 1, 2, ...,
  n } with root r, then its subtrees T_1 and T_2 are optimal BSTs for the 
  key { 1, 2, ..., r - 1 }and { r + 1, ..., n }, respectively.

- Note: items in a sub-problem are either a prefix or a suffix of the 
  original problem.

- Notation: for 1 <= i <= j <= n, let c_ij = weighted search cost of an 
  optimal BST for the items { i, i + 1, ..., j - 1, j }
    - with probabilities p_i, p_i + 1, ..., p_j
- Recurrence: 
    - for every 1 <= i <= j <= n:
        - C_ij = min (r = 1, j) { sum (k = 1, j) p_k + C_i_(r-1) + C_(r+1)_j }
        - recall formula C(T) = sum (k) p_k + C(T_1) + C(T_2)
        - interpret C_xy = 0 if x > y

- Correctness: optimal substructure narrows candidates down to (j - 1 + 1) 
  possibilities, recurrence picks the best by brute force.

- Important: solve smallest sub-problems (with the fewest number (j - i + 1) 
  of items) first.

- Let A = 2D Array
- For s = 0 to (n - 1): [s represents c_j - i_j]
    - For i = 1 to n: 
        - if i > r - 1, A[i, r - 1] = 0
        - if r + 1 > i + s, A[r + 1, i + s] = 0
        - A[i, i + s] = min (r = 1, i + s) [sum (k = 1, i + s) p_k + A[i, r 
          - 1], + A[r + 1, i + s]]

- Return A[1, n]

- Running Time: 
    - O(n^2) sub-problems
    - O(j - i) time to compute A[i, j]
    - O(n ^ 3) time overall
    - Not great.

- Fun Fact:
    - Optimized version of this DP algorithm correctly fills up table in 
      only O(n^2) time [O(1) on average per sub-problem]
    - Idea: piggyback on the work done in previous sub-problems to avoid 
      trying all possible roots. 
