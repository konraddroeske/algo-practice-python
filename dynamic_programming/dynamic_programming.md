## Characteristics of DP Problems

1. The problem will ask for the optimum value (min, max) of something.

- What is min cost of doing...
- What is the max profit...
- How many ways are there to do...
- What is the longest possible...
- Is it possible to reach a certain point...

2. Future decisions depend on earlier decisions.

- Greedy algorithms will often prevent us from finding the optimal solution,
  which relies on previous decisions.
- When trying to decide of this characteristic is applicable, assume it isn't,
  then think of a counterexample that proves a greedy algorithm doesn't work.
- If using one element prevents the usage of other elements, then we should consider
  using dynamic programming.

### More Info

- DP problems are used for problems with Optimal Substructure (can be broken down into sub-problems mathematically)
  and overlapping sub-problems.
- Divide and conquer can be parallelized, while DP problems cannot without significant complexity.
- When converting a top-down (recursive) to a bottom-up (tabulation), we can use the same base cases
  and relation, however bottom-up iterates over all the states such that each sub-problem has been solved
  before arriving at the current state.