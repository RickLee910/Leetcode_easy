class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.cur.right = node
                self.cur = node
                inorder(node.right)

        ans = self.cur = TreeNode(None)
        inorder(root)
        return ans.right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        result = []
        def find(root):
            if root:

                find(root.left)
                result.append(root.val)
                find(root.right)
        find(root)
        start = now = TreeNode(0)
        for r in result:
            now.right = TreeNode(r)
            now = now.right

        return start.right
'''
class Solution {
public:
    void


inOrder(TreeNode * root, vector < int > & res)
{
if (root == NULL)
return;
inOrder(root->left, res);
res.push_back(root->val);
inOrder(root->right, res);
}
TreeNode * increasingBST(TreeNode * root)
{
vector < int > res;
inOrder(root, res);
TreeNode * ans = new
TreeNode(0), *cur = ans;
for (int v:res)
    {
        cur->right = new
    TreeNode(v);
    cur = cur->right;
    }

    return ans->right;
    }
    };
'''
