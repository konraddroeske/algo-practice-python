## Master Method

Allows you to determine how divide and conquer will perform

### Algo #1: Grade School Algorithm

T(n) = max num of operations algo needs to multiply two n-digit numbers

Recurrence:

- Express T(n) in terms of running terms of recursive calls

Base case:

- T(1) <= a constant

General case:

- For all n > 1: T(n) <= 4 * T(n / 2) + O(n)

### Algo #2: Gauss

Recursively compute:

1. ac
2. bd
3. (a + b)(c + d), given ad + bc = 3 - 1 - 2

General case:

- For all n > 1: T(n) <= 3 * T(n / 2) + O(n)

### Recurrance Format

Assumptions:

- All sub-problems have equal size

1. Base Case: T(n) <= A constant for all sufficiently small n
2. For all larger n:
    - T(n) < a * T(n / b) + O(n ^ d)
    - a = num of recursive calls (n >= 1)
    - b = input size shrinkage factor (> 1)
    - d = exponent in running time of "combine step" (>= 0)
    - a, b, d are all constants

### The Master Method

If T(n) <= a * T (n / b) + O(n ^ d), then:

T(n) = {
O(n^d log n) if a = b ^ d (Case 1)
O(n ^ d) if a < b ^ d (Case 2)
O(n ^ (log b a)) if a > b ^ d (Case 3)
}

### Example #1 - Merge Sort

a = 2
b = 2
d = 1

Case 1 - a = b ^ d
T(n) <= O(n log n)

### Example #2 - Binary Search (like looking in a phone book)

a = 1
b = 2
d = 0 (Constant)

Case 1 - O(log n)

### Example #3 - Integer Multiplication

a = 4
b = 2
d = 1 (Linear)

Case 3 - O (n ^ log 2 4) = O (n ^ 2)

### Example #4 - Gauss' Trick

a = 3
b = 2
d = 1

Case 3 - O (n ^ log 2 3) - O (n ^ 1.59)

# Proof