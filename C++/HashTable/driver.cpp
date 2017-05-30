#include <iostream> 
#include <cassert> 
#include <string> 
#include "HashTable.h"

using namespace std; 

int main() {
	HashTable<int, string> his; 
	his.add(5, "five"); 
	his.add(10, "ten"); 
	his.add(20, "twenty"); 
	his.add(40, "forty"); 
	his.add(80, "eighty"); 

	assert(his.exists(10)); 
	assert(his.get(40) == "forty"); 
	assert(his[80] == "eighty"); 

	his.remove(20); 
	assert(his.size() == 4);
	assert(his.capacity() == 16); 
	
	his.add(1, "one"); 
	his.add(2, "two");
	his.add(3, "three");
	his.add(4, "four");
	his.add(5, "five");
	his.add(6, "six");
	his.add(7, "seven");
	his.add(8, "eight");
	his.add(9, "nine");
	his.add(10, "ten");
	his.add(11, "eleven");
	his.add(12, "twelve");
	his.add(13, "thirteen");
	his.add(14, "fourteen");
	
	// Table doubling should occur on this operation
	his.add(15, "fifteen"); 
	assert(his.size() == 17 && his.capacity() == 32); 

	return 0;
}
