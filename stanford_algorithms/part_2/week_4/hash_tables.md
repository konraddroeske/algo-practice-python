### Supported Operations

- Purpose:
    - Maintain a (possibly evolving) set of stuff.
        - transactions, people + associated data, IP addresses, etc.

- Using a "key":
    - Insert: add new record
    - Delete: delete existing record
    - Lookup: check for a particular record
    - Running Time: O(1)
        - If properly implemented
        - Non-pathological data (can't guarantee worst time)

- Does NOT maintain an ordering on elements, unlike Heap or Search Tree

- Application:
    - De-duplication problem
        - Given: A "stream" of objects.
            - Linear scan through a huge file
            - Or, objects arriving in real time
        - Goal: remove duplicates (i.e. keep track of unique objects)
            - e.g., report unique visitors to web site
            - avoid duplicates in search results
        - Solution: when new object arrives
            - lookup x in hash table (H)
            - if not found, insert x into hash table (H)
    - 2-Sum Problem
        - Unsorted array of n integers. Target sum t.
        - Goal: determine whether there are two numbers x, y in A
          with x + y = t
        - Naive solution: O(n ^ 2) time via exhaustive search
        - Better:
            1. Sort A (O(n log n) time)
            2. For each x in A, look for t - x in A via binary search (O(n
               log n))
        - Amazing:
            1. Insert elements of A into hash table H (O(1))
            2. For each x in A, look up t - x in H (O(n))
    - Symbol tables in compilers
    - Blocking network traffic (look up if ip in black list)
    - Search algorithms (e.g., game tree exploration)
        - Use hash table to avoid exploring any configuration (e.g., arrange
          of chess pieces) more than once

### Hash Table Implementation

### High-Level Idea

- Setup: universe U (e.g., all IP addresses, all names, all chess board
  configurations, etc.)
    - Generally, REALLY BIG

- Goal: want to maintain evolving set S in U
    - Generally, of reasonable size

- Naive Solutions
    1. Array-based solution (indexed by U)
        - O(1) operations, but O(|U|) space
    2. List-based solution
        - O(|S|) space, but O(|S|) lookup

- Solution:
    1. Pick n = # of "buckets" with n ~= |S|
        - For simplicity assume |S| doesn't vary much
    2. Choose a hash function h:
        - U -> {0, 1, 2, ..., n - 1}
    3. Use array A of length n, store x in A[h(x)]

- Collision: distinct x, y in U such that h(x) = h(y)
    - Solution #1: (separate) chaining
        - Keep linked list in each bucket
        - Given a key/object x, perform Insert/Delete/Lookup in a list in A[h
          (x)]
    - Solution #2: open addressing (only one object per bucket)
        - hash function now specifies probe sequence h_1(x), h_2(x), ...,
          (keep trying til find open slot)
        - Examples:
            - linear probing (look consecutively)
            - double hashing (use 2 hash functions, 2nd one used as offset)

- Note:
    - In hash table with chaining, Insert is O(1)
        - insert new object x at front of list in A[h(x)]
    - O(list(length)) for Lookup/Delete
        - could be anywhere from m / n (equal-length lists) to m (all
          objects in the same bucket) from m objects

- Point:
    - Performance depends on the choice of the hash function!
    - Analogous situation with open addressing

- Properties of a "good" Hash function:
    1. Should lead to good performance => i.e., should "spread data out"
       (gold standard: completely random hashing)
    2. Should be easy to store / very fast to evaluate

- Bad Hash Functions
    - Example: keys = phone numbers (10-digits)
        - |U| = 10 ^ 10
        - Choose n = 10 ^ 3
        - Terrible hash function:
            - h(x) = 1st 3 digits of x
            - Area codes are clumpy, some don't exist, lots of items in the
              same buckets
        - Mediocre hash function:
            - h(x) = last 3 digits of x
            - Still vulnerable to patterns in the last 3 digits
    - Example: keys = memory locations (will be multiples of 2)
        - Bad hash function:
            - h(x) = x % 1000 (again n = 10^3)
            - All odd buckets guaranteed to be empty

- Quick and Dirty Hash Functions
    - Objects ("hash code" ->) integers ("compression fn" ->) buckets {0, 1, 2,
      ..., n - 1}
        - Hash code (spread data out equally):
            - Can skip if already integers
            - If not numeric, string to int (sum ASCII code + constant +
              apply modulus)
        - Compression fn:
            - like the mod n function
        - How to choose n = # of buckets?
            - choose n to be a prime (within constant factor of # of objects
              in table)
            - not too close to power of 2
            - not too close to power of 10

### Pathological Data Sets and Universal Hashing Motivation

- Load of a Hash Table
    - Definition: the load factor of a hash table is:
        - a := # of objects in hash table / # of buckets of hash table
    - Note:
        1. a = O(1) is necessary condition for operations to run in constant
           time
        2. with open addressing, need a << 1
    - Upshot #1: for good Hash Table performance, need to control load.
    - Upshot #2: for good Hash Table performance, need a good hash function.
        - i.e., spreads data evenly across buckets
        - Ideal: use super-clever has function guaranteed to spread every
          data set evenly.
        - Problem: DOES NOT EXIST! (for every hash function, there is a
          pathological data set)
        - Reason: fix a hash function h: U -> {0, 1, 2, ..., n - 1} (assum
          |U| >> n)
            - Pigeonhole Principle: there exists a bucket i such that
              at least |U|/n elements of U hash to i under h
            - If data set drawn only from these, everything collides!

- Main point: can paralyze several real-world systems (e.g., network intrusion
  detection) by exploiting badly designed hash functions.
    - open source
    - overly simplistic hash function (easy to reverse engineer a
      pathological data set)

- Solutions:
    1. Use a cryptographic hash function (e.g., SHA-2)
        - infeasible to reverse engineer a pathological data set
    2. Use randomization
        - Design a family H of hash function such that, for all data sets S,
          "almost all" function h (in H) spreads s out "pretty evenly".
        - Compare to QuickSort guarantee

### Randomized Solution:

1. Proposed definition of a "good random hash function". (universal family
   of hash functions)
2. Concrete example of simple + practical such functions.
3. Justification of definition: "good functions" lead to "good performance"

### Bloom Filters

Raison d'etre: fast Inserts and Lookups

- Comparison to Hash Tables:
    - Pros: more space efficient
    - Cons:
        1. Can't store an associated object
        2. No deletions
        3. Small false positive probability (i.e., might say x has been
           inserted even though it hasn't been)

- Applications:
    - Original: early spellcheckers
    - Canonical: list of forbidden passwords
    - Modern: network routers
        - limited memory, need to be super-fast

- Under the hood:
    - Ingredients:
        1. array of n bits (so n / |s| = # of bits per object in data set S)
            - way less than storing a pointer to an object
        2. k hash functions h_1, ..., h_k (k = small constant)
    - Insert(x):
        - For i = 1, 2, ..., k:
            - Set A[h_i(x)] = 1 (whether bit already set to 1)
    - Lookup(x):
        - return TRUE <=> A[h_i(x)] = 1, for every i = 1, 2, ..., k
    - Note:
        - No false negative (if x was inserted, lookup(x) guaranteed to
          success)
        - But, false positive if all k h_i(x)'s already set to 1 by other
          insertions

- Is this a useful idea? Error probability must be small, when space per
  object is also small.

### Bloom Filters: Heuristic Analysis

- Intuition: should be a trade-off between space and error (false positive)
  probability.

- Assume: [not justified] all h_i(x)'s uniformly random and independent
  (across difference i's and x's)

- Setup: n bits, insert data set S into bloom filter

- Note: for each bit of A, the probability it's been set to 1 is (under the
  above assumption):
    - Recall: 1 + x is upper bounded by e^x
    - 1 - (1 - 1/n) ^ (k * |s|)
    - ~= 1 - e ^ ((-k * |s|) / n)
    - = 1 - e ^ (-k / b) (b = # of bits per object (n / |s|))
    - More bits, more space, smaller false positive probability

- Story so far: probability a given bit is 1 is <= 1 - e ^ (k / b)
- So: under assumption, for x not in s, false positive probability is:
    - <= [1 - e ^ (-k / b)] ^ k, where b = # of bits per object
    - Bigger b gets, smaller this probability

- How to set k?
    - For fixed b, Error Rate (E = [1 - e ^ (-k / b)] ^ k) is minimized by
      setting k ~= (ln 2) * b
        - Scales linearly with bits per object

- Plugging back in: E ~= (1 /2)^((ln 2) * b)
    - Goes down quickly as we scale b
    - b ~= 1.44 log 2 (1 / E)
     
- Ex: with b = 8, choose k = 5 or 6, error probability only ~= 2%
