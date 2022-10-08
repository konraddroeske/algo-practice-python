# Quick Sort

Input: Array of n numbers, unsorted.
Output: Same numbers, increasing order.
Assume: All array entries are distinct.

Exercise: Deal w/ duplicate entries.

Key idea: Partition array around a pivot element.

- Pick element of array (initially use first element)

- Rearrange array so that:
    - left of pivot -> less than pivot
    - right of pivot -> greater than pivot

Note: Puts pivot in its "rightful position".

Facts about partition:

1. Linear (O(n)) time, no extra memory.
2. Reduces problem size

## High level description

- Discovered by Tony Hoare (1961)

QuickSort(array A, length n)

- if n = 1 return
- p = ChoosePivot(A, n)
- Partition A around p
    - 1st part: less than P
    - 2nd part: greater than P
- Call quick sort on 1st part and 2nd part

## Partition Subroutine

Note: using O(n) extra memory, easy to partition around pivot in O(n)

### In-place Implementation

Assume: pivot = 1st element of array (if not, swap pivot w/ 1st element as preprocessing step)

High-level Idea:

- Single scan through array
- Invariant: everything looked at so far is partitioned

j = boundary b/w looked at and not looked at
i = boundary b/w less and greater than pivot

- Each step we advance j
- If A[j] is less than pivot, swap with A[i] (leftmost entry bigger than pivot), advance both
- else, advance j

Result: everything less than pivot, left of i, everything greater to the right of i

Running time = O(n), where n = r - l + 1 is the length of the input subarray
Reason: O(1) work per array entry
Also: clearly works in-place (repeated swaps)

Correctness:

- Claim: the for loop maintains the invariant:
    - A[l + 1], ..., A[i - 1] are all less than the pivot
    - A[i], ..., A[j - 1] are all greater than the pivot
- Consequence:
    - At end of for loop, everything less than pivot comes before everything greater than pivot.
    - After final swap, array partitioned around pivot.

## Inductive Review

let P(n) = assertion parameterized by positive integers n
For us, P(n) is "QuickSort correctly sorts every input array of length n"

How to prove P(n) for all n >= 1 by induction:

1. Base Case: P(1) -> assertion is true when n == 1
2. Inductive Step: for every n >= 2, prove that:
    - if P(k) holds for all k < n, then P(n) holds as well

Claim: P(n) holds for every n >= 1 (no matter how pivot is chosen)

1. Base Case -> every input array of length 1 is already sorted.
2. Inductive Step
    - Fix n >= 2
    - Need to show: if P(k) holds for all k < n, then P(n) holds as well.
    - Recall: QuickSort first partitions A around some pivot P.
    - Note: Pivot winds up in correct position.
    - let k1, k2 = length of 1st, 2nd parts of partitioned array (k1, k2 < n)
    - By inductive hypothesis: 1st, 2nd parts get sorted correctly by recursive calls.
    - So, after recursive calls, entire array correctly sorted.

## Choosing A Good Pivot

- Running time of QuickSort?
- Running time on input array that is already sorted:
    - O(n ^ 2)
- Running time when pivot perfectly selected:
    - O(n log n)

### Random Pivots

Intuition:

- If we always get a 25-75 split, good enough for O(n log n) running time. Prove via recursion tree.
- We don't need to be that lucky to get 25-75 split or better.

QuickSort Theorem: for every input array of length n, the avg running time of
QuickSort (with random pivots) is O(n log n).

Note:

- Holds for every input. (no assumptions on the data)
- Recall our guiding principles!
- "Average" is over random choices made by the algorithm