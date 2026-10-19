# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        cur = root

        while cur:
            if not cur.right:
                res.append(cur.val)
                cur = cur.left
            else:
                prev = cur.right
                while prev.left and prev.left != cur:
                    prev = prev.left

                if not prev.left:
                    res.append(cur.val)
                    prev.left = cur
                    cur = cur.right
                else:
                    prev.left = None
                    cur = cur.left

        res.reverse()
        return res