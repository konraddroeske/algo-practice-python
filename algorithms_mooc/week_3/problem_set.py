# Birthday Problem

# For each pair of people (i, j) of the k people in the room:
# Define the random variables X_ij for 1 <= i <= j <= k by,

# X_ij = I { person i and person j have the same birthday }
# I { 1 if person i and person j have the same birthday, 0 otherwise }

# E[X_ij] Pr { person i and person j have the same birthday } = 1 / n

# X = sum(k, i = 1) sum(k, j = i + 1) X_ij
# E[X] = E[ sum(k, i = 1) sum(k, j = i + 1) X_ij ]
# = sum(k, i = 1) sum(k, j = i + 1) E[X_ij]
# 1 = k (k - 1) / 2 * n
# 2 * 365 = k (k - 1)
# k = 28
