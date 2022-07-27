# input: a set of p = {p1, ..., pn} of n points in a plane (R^2)
# notation d(pi, pj) = Euclidian distance
# d(pi, pj) = sqrt((xi - yi)^2 + (xj - yj)^2)
# output: a pair p, q of distinct points that minimize d(p, q) over p

# Assumptions:
# no ties

# Brute Force: Double For Loop, over all pairs
# Running time: O(n^2)

# High level approach
# 1. Make copies of points sorted
# a) by x coords (Px)
# b) by y coords (Py)
# Run time: O(n log n)

# Divide into smaller sub problems
# Conquer sub-problems
# Combine solutions of sub-problems into one for the original problem

# base case, return below 2 points

# 1. let Q = left half of P, R = right half of P
# 2. (p1, q1) = closest pair of (Qx, Qy) - Left Side
# 3. (p2, q2) = closest pair of (Rx, Ry) - Right Side
# 4. Let D = min {d(p1, q1), d(p2, q2)}
# 5. (p3, q3) = ClosestSplitPair(Px, Py, D)
# 6. Return best of (p1, q1), (p2, q2), (p3, q3)

# key idea: only need to bother computing the closest split pair in "unlucky case"
# where its distance is less than d(p1, q1) and d(p2, q2).

# Closest Split Pair
# Requirements
# 1. O(n) time
# 2. Correct whenever closest pair of P is a split pair

# let x_bar = biggest x-coordinate in left of P
# let S_y = points of P w/ x-coordinate in [x_bar - D, x_bar + D], sorted by y coordinate.

# Init best = D, best_pair = null
# for i = 1 to |S_y| - 1
# for j = 1 to min { 7, |S_y| - i}
# let p, z = ith, (i + j)th points of S_y
# if d(p, q) < best:
# best_pair = (p, q), best = d(p, q)
