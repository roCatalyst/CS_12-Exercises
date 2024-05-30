from TreeNode import TreeNode
def count(root: TreeNode[int]) -> int:
    return 1 + sum(count(child) for child in root.children)

assert count(TreeNode(10, [])) == 1
assert count(TreeNode(10, [TreeNode(20, [])])) == 2
assert count(TreeNode(10, [TreeNode(20, []), TreeNode(30, [])])) == 3