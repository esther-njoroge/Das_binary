class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def preOrderTraversal(node):
    if node is None:
        return
    print(node.data, end=", ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)
    
root = TreeNode('R')
node1 = TreeNode('1')
node2 = TreeNode('2')
node3 = TreeNode('3')
node4 = TreeNode('4')
node5 = TreeNode('5')
node6 = TreeNode('6')
node7 = TreeNode('7')

root.left = node1
root.right = node2

node1.left = node3
node1.right = node4

node2.left = node5
node2.right = node6

node6.left = node7

# print(root.preOrderTraversal())
preOrderTraversal(root)
        