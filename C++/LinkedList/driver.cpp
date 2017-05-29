#include <iostream> 
#include <cassert> 
#include <string> 
#include "LinkedList.h"

using namespace std; 

// Testing LinkedList implementation
int main() {
	LinkedList<int> li; 
	assert(li.size() == 0 && li.empty());

	LinkedList<double> ld(5, -5.0); 
	assert(ld.at(4) == ld.front() == ld.back()); 
	
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
	assert(ls.front() == ls.back()); 

	ls.insert(0, "world!"); 
	ls.reverse(); 

	assert(ls.at(0) + " " + ls.at(1) == "Hello world!"); 

	return 0;
}
