public int max = 0;
/*
class Node 
int data;
Node left;
Node right;
*/
public int height(Node root) {
    return heightHelper(root, 0);
}

private int heightHelper(Node root, int curr) {
    int left = curr;
    int right = curr;
    if(root.left != null) {
        left = heightHelper(root.left, curr+1);
    }
    if(root.right != null) {
        right = heightHelper(root.right, curr+1);
    }
    return Math.max(left, right);
    
}

