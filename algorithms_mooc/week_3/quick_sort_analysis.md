## Decomposition Principle

### Preliminaries

- Fix input array A of length n.
- Big Omega = all possible random pivotes that QuickSort can choose
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

