# Depth First Search

# Pre Order - Process A, B, D
# In Order - Traverse A, B, D, then process D, B, E
# Post Order - Visit all children of node - D, E, B, F, G, C, A

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return "Node(" + str(self.value) + ")"


# SOLUTION #1 = Recursion using a stack, LIFO
# Pre order - print before walk
# In Order - print between walk
# Post order - print after walk

def walk(tree):
    if tree is not None:
        print(tree)
        walk(tree.left)
        walk(tree.right)


# SOLUTION #2 - Iterative Method

def walk2(tree, stack):
    stack.append(tree)

    while len(stack) > 0:
        node = stack.pop()
        if node is not None:
            print(node)
            stack.append(node.right)
            stack.append(node.left)


my_tree = Node('A',
               Node('B',
                    Node('D'),
                    Node('E')),
               Node('C',
                    Node('F'),
                    Node('G'))
               )

walk(my_tree)
print('\n')
walk2(my_tree, [])
