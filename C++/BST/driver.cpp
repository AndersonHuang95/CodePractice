#include <iostream>
#include <cassert>
#include <string>
#include "BST.h"

using namespace std;

int main() {
	BST<string> bst;
	assert(bst.getNodeCount() == 0); 

	bst.insert("honeydew"); 
	bst.insert("orange"); 
	bst.insert("banana"); 
	bst.insert("kiwi"); 
	bst.insert("watermelon"); 
	bst.insert("apple");
	bst.insert("boisinberry"); 
	bst.insert("pineapple"); 
	bst.insert("pear"); 
	bst.insert("tangerine"); 
	bst.insert("strawberry"); 
	bst.insert("raspberry"); 
	bst.insert("cherry");
	bst.insert("dragonfruit"); 
	bst.insert("canteloupe");
	bst.insert("blueberry"); 
	bst.insert("avocado"); 

	assert(bst.getNodeCount() == 17); 
	bst.print(); 
	bst.printAsTree(); 
	cout << bst.height(); 

	assert(bst.exists("banana")); 
	assert(bst.minValue() == "apple"); 
	assert(bst.maxValue() == "strawberry"); 

	assert(bst.getSuccessor("pear")->value == "pineapple"); 
	assert(bst.isBST()); 
	assert(bst.getSuccessor("banana")->value == "blueberry");

	return 0;
}
