## Grade School Algorithm

- input: 2 n-digit numbers x and y
- output: x * y
- primitive operation: add or multiply 2 single-digit numbers

- num of operations:
- 2n (multiply + carry) * n (for each number)
- Result: c * n ^ 2

### Can we do better?

## Karatsuba Multiplication

x = (10^(n / 2)) * a + b
y = (10^(n / 2)) * c + d
x * y = (10^n) * (a * c) + (10^(n / 2))((a * d) + (b * c)) + (b * d)

- Solve ac, ad, bc, db recursively
- Base case: 2 numbers w/ 1 digit each, multiply in one basic operation 

Step 1: recursively compute ac
Step 2: recursively compute bd
Step 3: recursively compute (a + b)(c + d) = ac + ad + bc + bd

Gauss' Trick: (3) - (1) - (2) = ad + bc