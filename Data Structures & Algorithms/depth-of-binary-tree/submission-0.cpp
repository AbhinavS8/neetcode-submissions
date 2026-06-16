/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int maxDepth(TreeNode* root) {
        int n1=1,n2=1;
        if (root==NULL) {
            return 0;
        }
        n1=maxDepth(root->left)+n1;
        n2=maxDepth(root->right)+n2;
        
        if (n1>n2) {
            return n1;
        }
        else {
            return n2;
        }
    }
};
