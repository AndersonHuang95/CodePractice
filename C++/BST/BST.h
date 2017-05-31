/* 
 * Implementation of a Binary Search Tree
 * The BST class is defined such that all nodes in the 
 * left subtree have values that are less than the root
 * and all nodes in the right subtree have values that are 
 * greater than or equal than the root.
 */ 

#ifndef BST_H
#define BST_h

#include <stdexcept> 
#include <iostream> 
#include <algorithm> // for max
#include <vector> 
#include <string> 
 
template <class T> 
class BST {
public:
	struct TreeNode<T> {
		TreeNode<T>(T val) : value(val), left(nullptr), right(nullptr) {}
		T value; 
		TreeNode<T> *left; 
		TreeNode<T> *right; 
	}

	BST(); 
	~BST();
	
	/* Accessors */ 
	int getNodeCount() const; 
	void print() const; 
	void printAsTree() const; 
	bool exists(T value) const;
	int height() const; 
	T minValue() const; 
	T maxValue() const; 
	bool isBST() const; 
	TreeNode<T> *getSuccessor(T value) const; 
	bool empty() const; 

	/* Mutators */
	void insert(T value); 
	void remove(T value);
	void deleteTree(TreeNode<T> *root); 
private:
	TreeNode<T> *find(TreeNode<T> *root, T value) const;
	TreeNode<T> *findMin(TreeNode<T> *root) const; 
	void printHelper(TreeNode<T> *root) const;
	bool existsHelper(TreeNode<T> *root, T value) const; 
	int heightHelper(TreeNode<T> *root) const; 
	T minValueHelper(TreeNode<T> *root) const; 
	T maxValueHelper(TreeNode<T> *root) const; 
	bool isBSTHelper(TreeNode<T> *root) const; 
	bool isSubtreeLesser(TreeNode<T> *root, T value) const; 
	bool isSubtreeGreater(TreeNode<T> *root, T value) const; 
	TreeNode<T> *getSuccessorHelper(TreeNode<T> *root, T value) const; 
	TreeNode<T> *insertHelper(TreeNode<T> *root, T value); 
	bool removeHelper(TreeNode<T> *root, T value, TreeNode<T> *parent); 
	
	Node *m_root; 
	int m_nodes; 
};

template <class T>
BST<T>::BST() : m_root(nullptr), m_nodes(0) {}

/* Deleting all nodes entails postorder traversal */
template <class T>
BST<T>::~BST() {
	deleteTree(m_root); 
}

template <class T>
int BST<T>::getNodeCount() const {
	return m_nodes; 
}

template <class T> 
void BST<T>::print() const {
	printHelper(m_root); 
	std::cout << std::endl; 
}

template <class T>
void BST<T>::printAsTree() const {
	std::vector<std::vector<T>> tree;
	if (!m_root) return tree;
	std::queue<TreeNode<T>> q; 
	q.push(m_root); 
	q.push(nullptr); 

	std::vector<T> v; 
	
	while(!q.empty()) {
		TreeNode<T> *current = q.front();
		q.pop();

		// Use marker nullptr to mark level separation
		if (current == nullptr) {
			tree.push_back(v); 
			v.resize(0);
			if (q.size() > 0) q.push(nullptr); 
		}
		else {
			v.push_back(current->value); 
			if (current->left) q.push(current->left); 
			if (current->right) q.push(current->right);
		}
	}
	 
	for (int i = tree.size() - 1; i >= 0; --i) {
		for (int j = 0; j < tree[i].size(); ++j) {
			if (j == 0) cout << std::string(i, ' ') << tree[i][j]; 
			std::cout << tree[i][j] << " ";
		}
		std::cout << std::endl;
	}
}

template <class T>
bool BST<T>::exists(T value) const {
	return existsHelper(m_root, value); 
}

template <class T>
int BST<T>::height() const {
	return heightHelper(m_root); 
}

template <class T>
T BST<T>::minValue() const {
	return minValueHelper(m_root); 
}

template <class T>
T BST<T>::maxValue() const {
	return maxValueHelper(m_root);
}

template <class T>
bool BST<T>::isBST() const {
	return isBSTHelper(m_root); 
}

template <class T>
TreeNode<T> *BST<T>::getSuccessor(T value) const {
	return getSuccessorHelper(m_root, value); 
}

template <class T> 
bool BST<T>::empty() const {
	return m_nodes == 0; 
}

template <class T>
void BST<T>::insert(T value) {
	insertHelper(m_root, value); 
}

template <class T>
void BST<T>::remove(T value) {
	removeHelper(m_root, value); 
}

template <class T>
void BST<T>::deleteTree(TreeNode<T> *root) {
	if (!root) return; 
	deleteTree(root->left); 
	deleteTree(root->right);
	// Do something goes here
	std::cout << root->value << " "; 
}

/* 
 * Start of private helper functions 
 */ 

template <class T>
TreeNode<T> *BST<T>::find(TreeNode<T> *root, T value) const {
	if (!root) return nullptr;

	if (root->value == value) return root; 
	else if (value < root->val) return find(root->left, data);
	else return find(root->right, data); 
}

template <class T>
TreeNode<T> *BST<T>::findMin(TreeNode<T> *root) const {
	if (!root->left) return root; 
	return findMin(root->left); 
}

template <class T> 
void BST<T>::printHelper(TreeNode<T> *root) const {
	 // Recursion bottoms out here
	 if (!root) return; 

	 printHelper(root->left); 
	 std::cout << root->value << " "; 
	 printHelper(root->right); 
}

/* O(h) operation, where h is the height of the tree */ 
template <class T>
bool BST<T>::existsHelper(TreeNode<T> *root, T value) const {
	// Base cases
	if (!root) return false; 
	if (value == root->value) return true; 
	
	if (value < root->value) {
		// Explore left subtree
		return exists(root->left);
	}
	else {
		// Explore right subtree 
		return exists(root->right); 
	}
}

/* O(h) operation
 * a tree with a single node is defined as having height 0
 * the height then is equal to the number of edges following 
 * the longest path from root to a leaf node 
 *
 *        0
 *     -------
 *     |     |
 *     1     2
 *  ------ ------
 *  |    | |    |
 *  N    N 3    4
 * 
 * For example, the above tree will recursively call height 
 * on its two subtrees
 * (root's LEFT subtree) The recursion returns (-1) for Node #1's left and right subtrees 
 * Subsequently, 1 is returned for the LEFT side
 * (root's RIGHT subtree) The recursion returns (-1) for Node #3 and #4's left and right 
 * Tracing up, there is a height of 2 
 * 
 */
template <class T>
int BST<T>::heightHelper(TreeNode<T> *root) const {
	if (!root) return -1; 
	return (std::max(height(root->left), height(root->right)) + 1); 
}

/* Find the left-most node */
template <class T>
T BST<T>::minValueHelper(TreeNode<T> *root) const {
	if (m_nodes == 0) throw std::out_of_range("Cannot seek min value of an empty tree"); 
	
	if (root->left == nullptr)
		return root->value; 
	minValueHelper(root->left); 
}

/* Find the right-most node */ 
template <class T>
T BST<T>::maxValueHelper(TreeNode<T> *root) const {
	if (m_nodes == 0) throw std::out_of_range("Cannot seek max value of an empty tree"); 

	if (root->right == nullptr) 
		return root->value;
	maxValueHelper(root->right); 
}

template <class T>
bool BST<T>::isBSTHelper(TreeNode<T> *root) const {
	if (!root) return true; 
		
	return isSubtreeLesser(root, root->value) 
		&& isSubtreeGreater(root, root->value)
		&& isBSTHelper(root->left) 
		&& isBSTHelper(root->right); 

}

template <class T>
bool BST<T>::isSubtreeLesser(TreeNode<T> *root, T value) const {
	if (!root) return true; 

	return (root->value < value
		&& isSubtreeLesser(root->left, value)
		&& isSubtreeLesser(root->right, value));
}

template <class T>
bool BST<T>::isSubtreeGreater(TreeNode<T> *root, T value) const {
	if (!root) return true; 

	return (root->value >= value
		&& isSubtreeGreater(root->left, value)
		&& isSubtreeGreater(root->right, value));

}

/* 
 * O(h) 
 * Returns pointer to node that is a successor
 * nullptr if none exists 
 * this happens if all nodes have values smaller
 * or the node with value does not exist
 */ 
template <class T>
TreeNode<T> *BST<T>::getSuccessorHelper(TreeNode<T> *root, T value) const {
	Node *current = find(root, data); 
	if (!current) return nullptr;

	// Two cases
	// right subtree exists 
	if (current->right) 
		return findMin(current->right); 
	
	// right subtree does not exist
	else {
		Node *successor = nullptr; 
		Node *ancestor = root; 
		
		// Search until ancestor's data becomes smaller than current's
		// Return the node right before this situation occurs 
		// To do this, keep candidates in a variable, successor
		// Successor is only updated when ancestor's values are 
		// greater than or equal to current->data 
		while (ancestor != current) {
			if (current->data < ancestor->value) {
				successor = ancestor;
				ancestor = ancestor->left; 
			}
			else ancestor = ancestor->right; 
		}	
		return successor; 
	}
}

/* O(h) 
 * Duplicate values are allowed
 */
template <class T>
TreeNode<T> *BST<T>::insertHelper(TreeNode<T> *root, T value) {
	// Special case is insertion into empty try 
	if (m_nodes == 0) {
		TreeNode<T> *tmp = new TreeNode<T>(value);
		m_root = tmp; 
		++m_nodes;
		return m_root; 
	}
	
	// Base case 
	if (!root) {
		TreeNode<T> *tmp = new TreeNode<T>(value); 
		++m_nodes; 
		return tmp; 
	}
	
	// Recursive cases
	if (value < root->value) root->left = insertHelper(root->left, value); 
	else root->right = insertHelper(root->right, value);

	return root; 
}

/* O(h) 
 * removeHelper
 * returns true if deletion was successful 
 */
template <class T>
bool *BST<T>::removeHelper(TreeNode<T> *root, T value, TreeNode<T> *parent) {
	// Empty tree
	if (m_nodes == 0) throw std::out_of_range("Cannot remove from empty tree"); 
	
	// Value does not exist 
	if (!root) return false; 

	if (value < root->value) {
		return removeHelper(root->left, value, root); 
	}
	else if (value > root->value) {
		return removeHelper(root->right, value, root); 
	}
	else {
		// Leaf
		if (!root->left && !root->right) {
			delete root; 

			// Single element tree 
			if (!parent) { 
				m_root = nullptr; 
				return true;
			}

			// Which kind of child is root?
			(parent->left == root) ? parent->left == nullptr : parent->right == nullptr;
		}
		// One child
		else if (!root->left || !root->right) {
			TreeNode<T> *tmp = (root->left) ? root->left : root->right; 
			(parent->left == root) ? parent->left = tmp : parent->right = tmp; 
			delete root; 
		}
		// Two children
		else {
			T tmp = minValueHelper(root->right); 

			// a) Left subtree of root's right subtree exists 
			// Find the smallest of the largest in tree rooted at root->right

			// b) Right subtree has no left subtree
			// Swap the two values, then delete (root->right) 
			
			// Either cases are handled recursively 
			removeHelper(root->right, tmp, root); 
			root->val = tmp; 
		}

		return true; 
	}
}

#endif // BST_H
