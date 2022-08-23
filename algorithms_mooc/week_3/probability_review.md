## Probability Review 1

### Sample Spaces

- Big Omega = "All possible outcomes" which is usually finite.
- Each outcome has a probability p(i) > 0
- Constraint: Sum of p(i)  = 1

- Ex. #1 - Rolling 2 Dice:
    - Big Omega = { (1, 1), (2, 1), ... (5, 6), (6, 6) } -> 36 Ordered Pairs
    - p(i) = 1 / 36 for all i

- Ex. #2 - Choosing a random pivot in outer QuickSort call.
    - Big Omega = { 1, 2, ..., n } (index of pivot)
    - p(i) = 1 / n for all i

### Events

- An event is a subset S of Big Omega
- The probability of an event S = sum of p(i), with i in S

### Random Variables

- A random variable X is a real valued function X: Big Omega -> Real Number
- We usually care about running time of a random variable.

- Ex. #1:
    - Sum of the two dice.
- Ex. #2:
    - Size of the subarray passed to the 1st recursive call.

### Expectation

- Expected Value of X = average value of X
- Sum of values * p(i)

### Linearity of Expectation

- let x_1, ..., x_n be random variables defined on Big Omega
- Then:
    - Expected Value of ALL x_i = Sum of EACH Expected Value of x_i

### Load Balancing

- Problem: need to assign n processes to n servers. 
- Proposed Solution: assign each process to a random server.
- Question: What is the expected number of processes assigned to a server?
- Solution:
  - Sample Space Big Omega = all n^n assignments of processes to servers, each equally likely.
  - let Y = total number of processes assigned to the first server.
  - Goal: compute expected value of Y
  - Let x_j = { 1 if jth process assigned to the first server, 0 otherwise }
    - "indicator random variable" 
    - Note: Y = Sum of x_j (j = 1 to n)

### Probability Review 2