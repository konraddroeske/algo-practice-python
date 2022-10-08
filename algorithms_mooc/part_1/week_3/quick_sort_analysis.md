## Decomposition Principle

### Preliminaries

- Fix input array A of length n.
- Big Omega = all possible random pivots that QuickSort can choose
- Key random variable, for s in Big Omega:
    - C(s) = # of comparisons between two input elements made by QuickSort,
      given random choices of s

- Lemma: running time of QuickSort dominated by comparisons.
    - There exists a constant c so that total num of operations of ANY type, is at
      most a constant factor larger than the number of comparison.
    - RT(s) <= c * C(s)

- Remaining goal: E[C] = O(n log n)

### Building Blocks

- Master Method does not apply:
    - Size of sub-problems is random
    - Unbalanced sub-problems

A = fixed input array

Notation:

- z_i = ith smallest element of A, wherever it may lie in array

For s in Big Omega, indices i < j, let:

- X_ij(s) = # of times z_i, z_j get compared in QuickSort w/ pivot sequence s

- Two elements at most get compared once:
    - Two elements only get compared when one is the pivot, which is then excluded from
      future recursive calls.
    - Thus, each X_ij is an "indicator" (0, 1) random variable.

- So:
    - C(s) = # of comparisons b/w input elements
    - X_ij(s) = # of comparisons b/w z_i and z_j
- Thus:
    - C(s) = Sum(n - 1, i = 1) Sum(n, j = i + 1) X_ij(s)
- By linearity of expectation:
    - E[C] = Sum(n - 1, i = 1) Sum(n, j = i + 1) E[X_ij]
    - E[X_ij] = Pr[x_ij = 1]
    - E[C] = Sum(n - 1, i = 1) Sum(n, j = i + 1) Pr[z_i, z_j get compared]

### General Decomposition Principle

1. Identify random variable Y that you really care about.
2. Express Y as sum of indicator random variables:
    - C = Sum(m, l = 1) X_l
3. Apply linearity of expectations:
    - E[Y] = Sum(m, l = 1) Pr[X_l = 1]

### Proof

Recall:

- E[C] = sum(n - 1, i = 1) sum(n, j = i + 1) Pr[X_ij = 1] = Pr[z_i, z_j get compared]

Key Claim:

- For all pairs of elements i < j, Pr[z_i, z_j get compared] = 2 / (j - i + 1)

How do we prove?

- Fix z_i, z_j with i < j (3rd smaller, 7th smallest elements in array)
- Consider the set z_i, z_i+1, ..., z_j-1, j_j
- Inductively:
    - As long as none of these chosen as a pivot, all are passed to the same recursive call.
    - Consider the first amount z_i, z_i+1, ..., z_j+1, z_j that gets chosen as a pivot.
        - if z_i or z_j gets chosen first, they are definitely compared.
        - if z_i+1, ..., z_j-1 gets chosen first, then z_i & z_j are **never compared**.

1. z_i or z_j chosen first -> they get compared
2. one of z_i+1, ..., z_j-1 chosen first -> z_i, z_j never compared

Note: Since pivots always chosen uniformly at random, each of z_i, z_i+1, ..., z_j-1, z_j is equally likely to be the
first.

-> Pr[z_i, z_j get compared]  
= (# of pivot choices that lead to comparison) / (# of pivot choices overall)
= 2 / (j - i + 1)

So, avg num of comparisons for array of length n:
E[C] = sum(n - 1, i = 1) sum(n, j = i + 1) (2 / (j - i + 1))
-> E[C] = 2 * sum(n - 1, i = 1) sum(n, j = i + 1) (1 / (j - 1 + 1))

Note: For each fixed i, the inner sum is:

- sum(n, j = i + 1) (1 / (j - 1 + 1)) = 1/2 + 1/2 + 1/4 + ... + 1/n
  -> sum(n, k = 2) (1 / k)

So,
E[C] <= 2 * (n - 1) * sum(n, k = 2) (1 / k)
-> 2 * (n) * sum(n, k = 2) (1 / k) (simplify n - 1 to n)

Claim: sum(n, k = 1) (1 / k) is logarithmic of n (<= ln n)

-> O(2n ln n) -> O(n log n)