# X * Y = Z
# Z ij = (ith row of X) * (jith row of Y) = sum k=1 (X ik * Y kj)
# Running time: O(n ^ 2)

# n = 2
# X = [[a, b], [c, d]]
# Y = [[e, f], [g, h]]
# Z = [[ae + bg, af + bh], [ce + dg, cf + dh]]
# Running time: O(n ^ 3)

# Idea: Split into smaller quadrants recursively

# Step 1: Recursively compute the 8 necessary products.
# Step 2: Do the necessary additions - O(n ^ 2)

# Run time is O(n ^ 3) - not better or worse than straightforward algorithm

# Strassen's Algorithm (1969)
# Step 1: Recursively compute only 7 (cleverly chosen) products
# Step 2: Do the necessary (clever) additions + subtractions (still O(n ^ 2) time)
# Fact: Better than cubic time (see master method)

# The 7 Products

# X = ( A B, C D)
# Y = ( E F, G H)

# P1 = A * (F - H)
# P2 = (A + B) * H
# P3 = (C + D) * E
# P4 = D * (G - E)
# P5 = (A + D) * (E + H)
# P6 = (B - D) * (G + H)
# P7 = (A - C) * (E + F)

# Claim:
# X * Y = [[P5 + P4 - P2 + P6, P1 + P2], [P3 + P4, P1 + P5 - P3 - P7]]

