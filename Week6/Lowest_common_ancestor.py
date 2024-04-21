class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or p == root or q == root:
            return root

		# recursively check both sides of the children of this current node
        left  = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

		# if we found BOTH p and q, we're done! return this node, it's the LCA
        if left and right:
            return root

		# otherwise, return "left" or "right". This will either return: None, P, or Q
        return left or right
        