class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
count=0

def countSingleRec(root):
    #Return false to indicate NULL
    if (root == None):
        return True
    
    # Recursively count in left and right subtrees also
    left = countSingleRec(root.left)
    right = countSingleRec(root.right)
    
    #If any of the subtrees is not singly, then this cannot be singly.
    if (left == False and right == False):
       return False
    
    #If left subtree is singly and non-empty, but data doesn't match
    if (root.left and root.data != root.left.data):
        return False
    
    #Same for right subtree
    if (root.right and root.data != root.right.data):
        return False
    
    # If none of the above conditions is true, then tree rooted under
    # root is single valued, increment count and return true.
    global count
    count+=1
    return True

def countSingle(root):
    
    # Recursive function to count
    countSingleRec(root)
    return count


# Let us construct the below tree
#           5
#         /   \
#       4      5
#     /  \      \
#    4    4      5

root = Tree()
root.data = 5
root.left = Tree()
root.left.data = 4
root.right = Tree()
root.right.data = 5
root.left.left = Tree()
root.left.left.data = 4
root.left.right = Tree()
root.left.right.data = 4
root.right.right= Tree()
root.right.right.data= 5
print("Count of Single Valued Subtrees is ",countSingle(root))
