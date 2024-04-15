class currentNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

 
def findMax(root):
 
    
    if (root == None):
        return float('-inf')
 
   
    ans = root.data
    lans = findMax(root.left)
    rans = findMax(root.right)
    if (lans > ans):
        ans = lans
    if (rans > ans):
        ans = rans
    return ans
 
 
if __name__ == '__main__':
    root = currentNode(2)
    root.left = currentNode(7)
    root.right = currentNode(5)
    root.left.right = currentNode(6)
    root.left.right.left = currentNode(2)
    root.left.right.right = currentNode(11)
    root.right.right = currentNode(9)
    root.right.right.left = currentNode(4)
 
    
    print("Maximum element is",
          findMax(root))
    
                    
