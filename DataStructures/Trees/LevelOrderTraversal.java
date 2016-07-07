/* 
class Node 
int data;
Node left;
Node right;
*/
void LevelOrder(Node root)
{
    LinkedList<Node> q = new LinkedList<Node>();
    q.addLast(root);
    while(!q.isEmpty()) {
        Node temp = q.poll();
        System.out.print(temp.data + " ");
        if (temp.left != null) q.addLast(temp.left);
        if (temp.right != null) q.addLast(temp.right);
    }

}

