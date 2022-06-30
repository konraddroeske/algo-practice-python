# Asymptotic Analysis

### Importance

- Vocabulary for the design and analysis of algorithms
- For high-level reasoning about algorithms
- Coarse enough to suppress architecture/language/compiler dependent details
- Sharp enough to make useful comparisons b/w diff algos, esp. on large inputs
    - Sorting, integer multiplication, etc.

### High Level Idea

- Suppress constant factors and lower-order terms.
- Constant factors too system dependent.
- Lower-order terms become irrelevant for large inputs.

### Example 1

- 6n log n + 6n becomes n log n
- Running time is O (n log n) where n is input size

