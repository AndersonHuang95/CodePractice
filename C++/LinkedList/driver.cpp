#include <iostream> 
#include <cassert> 
#include <string> 
#include "LinkedList.h"

using namespace std; 

// Testing LinkedList implementation
int main() {
	LinkedList<int> li; 
	assert(li.size() == 0 && li.empty());

	LinkedList<string> ls; 
	ls.push_back("Hello"); 
	ls.push_back("there"); 
	ls.push_back("world!");
	assert(ls.size() == 3); 

	ls.push_front("I say"); 
	ls.remove("I say"); 
	assert(ls.size() == 3); 

	ls.erase(1); 
	ls.erase(1);  

	ls.insert(0, "world!"); 
	ls.reverse();  

	return 0;
}
