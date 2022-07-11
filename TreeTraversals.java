public class TreeTraversals {
    class Node{
        int data;
        Node right=null;
        Node left=null;
        public Node(int data){
            this.data=data;
        }
    }
    public static void traverseInOrder(Node root){
        Node t=root;
        while(t!=null){
            traverseInOrder(t.left);
            System.out.println(t.data);
            traverseInOrder(t.right);
        }
    }
    public static void preOrderTraversal(Node root){
        Node t=root;
        while(t!=null){
            System.out.println(t.data);
            preOrderTraversal(t.left);
            preOrderTraversal(t.right);
        }
    }
    public static void postOrderTraversal(Node root){
        Node t=root;
        while(t!=null){
            postOrderTraversal(t.left);
            postOrderTraversal(t.right);
            System.out.println(t.data);
        }
    }
}
