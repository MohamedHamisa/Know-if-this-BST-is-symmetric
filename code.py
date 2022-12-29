class Solution:   
 def isSymmetric(self, root):
        def isSym(L,R):
            if not L and not R: return True #Both of them are Null so it's symmetric
            if L and R and L.val == R.val: 
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return False
        return isSym(root, root)
