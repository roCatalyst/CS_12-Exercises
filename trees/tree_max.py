from TreeNode import TreeNode
def tree_max(root: int) -> int:
    ret: int = root.value
    for child in root.children:
        ret = max(ret, tree_max(child))

    return ret

assert tree_max(TreeNode(10, [])) == 10
assert tree_max(TreeNode(10, [TreeNode(20, [])])) == 20
assert tree_max(TreeNode(20, [TreeNode(10, [])])) == 20