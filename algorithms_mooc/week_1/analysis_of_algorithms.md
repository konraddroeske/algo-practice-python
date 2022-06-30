# Analysis of Algorithms

## Guiding Principles:

### Worst Case Analysis

- Our running time bound holds for every input of length n.
- Appropriate for "general purpose" routines.
- As opposed to:
    - "Average Case" analysis
    - Benchmarks
    - These require domain knowledge.
- Worst case usually easier to analyze.

### Won't pay attention to constant factors, lower-order terms

- Justifications:
    - Easier mathematically
    - Constants depend on architecture / compiler / programmer
    - Lose little predictive power

### Asymptotic Analysis

- Focus on large input size
- Justifications:
    - Only big problems are interesting.

### Holy Grail: Linear running time (or close to it).