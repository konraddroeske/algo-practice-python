### Problem

Input: array A with n distinct numbers and a number i { 1, 2, ..., n}

Output: ith order statistic (i.e., ith smallest element of input array)

Example: Median

- i = n + 1 / 2 for n odd
- i = n / 2 for n even

O(n log n) Algorithm:

- Apply mergesort
- Return ith element of sorted array

Fact: can't sort any faster thank O(n log n)

However, we can get O(n) time (randomized) by modifying QuickSort.

RSelect(array A, length n, order statistic i)

1. If n = 1, return a[0]
2. Choose pivot p from A, uniformly at random
3. Partition A around pivot, get 1st Part and 2nd Part
    - let j = new index of p

4. If j = i, return p
5. if j > 1, return RSelect(1st Part of A, j - 1, i)
6. if j < i, return RSelect(2nd Part of A, n - j, i - j)

Running Time:

- Could be as bad as O(n^2)
- Key: Find pivot giving "balanced" split
- Best pivot: The median! (but this is circular)
- Would get recurrence T(n) <= T(n / 2) + O(n)
- T(n) = O(n) -> Case 2 of the Master Method

Hope: Random pivot is "pretty good" "often enough".

### RSelect Theorem:

- For every input array of length n, the avg. running time of RSelect is O(n)
- Holds for every input (no assumptions on data)
- "average" is over random pivot choices made by the algorithm.

### Proof

- Note: RSelect uses <= c * n operations outside the recursive call (for some constant c > 0)
    - From partitioning.

Notation: RSelect is in phase j if current array size between:

- (3/4)^(j+1) * n and (3/4)^j * n
- Phase j quantifies the number of times we've made 75% progress relative to the original array

- X_j = avg number of recursive calls during phase j

Note: Running time of RSelect <= Sum(phases j) X_j * c * (3/4)^j * n

Note: if RSelect chooses a pivot giving a 25-75 split (or better), the current phase ends!

- New subarray length at most 75% of old length

Recall:

- Probability of 25-75% split or better is 50%.
  So:
- E[X_j] <= expected number of times you need to flip a fair coin to get one "heads".
- "heads" = good pivot, "tails" = bad pivot

Let N = num of coin flips until you get "heads"
- A "geometric random variable"

Note: E[N] = 1 + 1/2 * E[N]
- 1 = 1st coin flip
- 1/2 = probability of tails
- E[N] = # of further flips needed in this case

E[N] - (1/2 * E[N]) = 1
E[N] * (1 - 1/2) = 1
E[N] = 2

Recall: E[X_j] <= E[N] -> E[X_j] <= 2

Expected Running Time of RSelect 
<= E[c * n Sum(phase j) (3/4)^j X_j]
= c * n Sum(phase j) (3/4)^j E[X_j] (Linearity of Expectations)
<= 2 * c * n Sum(phase j) (3/4)^j (Geometric sum, <= 1 / (1 - 3/4) = 4
<= 8 * c * n
= O(n)