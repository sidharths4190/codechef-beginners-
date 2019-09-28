class BinarySearchTree{
	class Node{
		int key;
		Node left,right;
		int p;
		
		public Node(int item){
			key = item;
			left = right = null;
			p = 0;
		}
	}

	Node root;
	BinarySearchTree(){
	root = null;
}}

	 void insert(int key) { 
       root = insertRec(root, key); }
       
    Node insertRec(Node root, int key) { 
  
        
        if (root == null) { 
            root = new Node(key); 
	    
            return root; 
        } 
  
        
        if (key < root.key) 
            root.left = insertRec(root.left, key); 
        else if (key > root.key) 
            root.right = insertRec(root.right, key); 
  
        
        return root; 
    }

void delete(int key) {
    root = deleteRec(root, key);
}

Node deleteRec(Node node, int key) {
    // If tree is empty or node doesn't exist, return null.
    if (node == null) return null;

    // Else, recursively traverse the tree.
    if (key < node.key) {
        node.left = deleteRec(node.left, key);
    } else if (key > node.key) {
        node.right = deleteRec(node.right, key);
    } else {
        
        if (node.left == null)
            return node.right;
        else if (node.right == null)
            return node.left;

        
        node.key = minValue(node.right);

        
        node.right = deleteRec(node.right, node.key);
    }

    return node;
}

int minValue(Node node) {
    while (node.left != null) node = node.left;
    return node.key;
}
 static void main(String[] args) { 
        BinarySearchTree tree = new BinarySearchTree(); 
  
        
        tree.insert(5); 
        tree.insert(3); 
        tree.insert(4); 
        tree.insert(1); 
     
}
