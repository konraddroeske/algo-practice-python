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

Definition and Interpretation of NP-Completeness 1 - 7:55
