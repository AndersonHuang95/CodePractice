/* 
 * Implementation of a Binary Search Tree
 * Similar to C++ STL map 
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

template <class T> 
class BST {
public:
	struct TreeNode {
		TreeNode(T val) : value(val), left(nullptr), right(nullptr) {}
		T value; 
		TreeNode *left; 
		TreeNode *right; 
	}

	BST(); 
	~BST();
	
	/* Accessors */ 
	int getNodeCount() const; 
	void print() const; 
	bool exists(T value) const;
	int height() const; 
	T minValue() const; 
	T maxValue() const; 
	bool isBST() const; 
	T getSuccessor(T value) const; 
	bool empty() const; 

	/* Mutators */
	void insert(T value); 
	void remove(T value);
	void deleteTree(TreeNode *root); 
private:
	void printHelper(TreeNode *root) const;
	bool existsHelper(TreeNode *root, T value) const; 
	int heightHelper(TreeNode *root) const; 
	T minValueHelper(TreeNode *root) const; 
	T maxVAlueHelper(TreeNode *root) const; 
	bool isBSTHelper(TreeNode *root) const; 
	T getSuccessorHelper(TreeNode *root, T value) const; 
	void insertHelper(TreeNode *root, T value); 
	void removeHelper(TreeNode *root, T value); 
	
	Node *m_root; 
	int m_nodes; 
};

template <class T>
BST<T>::BST() : m_nodes(0) {}

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
void BSt<T>::print() const {
	printHelper(m_root); 
	std::cout << std::endl; 
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
T BST<T>::getSuccessor(T value) const {
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
void BST<T>::deleteTree(TreeNode *root) {
	if (!root) return; 
	deleteTree(root->left); 
	deleteTree(root->right);
	// Do something goes here
	std::cout << root->value << " "; 
}

/* 
 * Start of private helper functions 
 */ 

/* printing of tree returns an inorder traversal */ 
template <class T> 
void BSt<T>::printHelper(TreeNode *root) const {
	 // Recursion bottoms out here
	 if (!root) return; 

	 printHelper(root->left); 
	 std::cout << root->value << " "; 
	 printHelper(root->right); 
}

/* O(h) operation, where h is the height of the tree */ 
template <class T>
bool BST<T>::existsHelper(TreeNode *root, T value) const {
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
int BST<T>::heightHelper(TreeNode *root) const {
	if (!root) return -1; 
	return (std::max(height(root->left), height(root->right)) + 1); 
}

/* Find the left-most node */
template <class T>
T BST<T>::minValueHelper(TreeNode *root) const {
	if (m_nodes == 0) throw std::out_of_range("Cannot seek min value of an empty tree"); 
	
	if (root->left == nullptr)
		return root->value; 
	minValueHelper(root->left); 
}

/* Find the right-most node */ 
template <class T>
T BST<T>::maxValueHelper(TreeNode *root) const {
	if (m_nodes == 0) throw std::out_of_range("Cannot seek max value of an empty tree"); 

	if (root->right == nullptr) 
		return root->value;
	maxValueHelper(root->right); 
}

template <class T>
bool BST<T>::isBSTHelper(TreeNode *root) const {
	return isBSTHelper(m_root); 
}

template <class T>
T BST<T>::getSuccessorHelper(TreeNode *root, T value) const {
	return getSuccessorHelper(m_root, value); 
}

template <class T>
void BST<T>::insertHelper(TreeNode *root, T value) {
	insertHelper(m_root, value); 
}

template <class T>
void BST<T>::removeHelper(TreeNode *root, T value) {
	removeHelper(m_root, value); 
}

#endif // BST_H
