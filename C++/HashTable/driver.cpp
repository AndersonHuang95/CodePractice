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
	
	his[1] = "one"; 
	his[2] = "two"; 
	his[3] = "three";
	his[4] = "four";
	his[5] = "five"; // testing overwrite property
	his[6] = "six";
	his[7] = "seven";
	his[8] = "eight";
	his[9] = "nine"; 
	his[10] = "ten";
	his[11] = "eleven";
	his[12] = "tweleve";
	his[13] = "thirteen";

	// Table doubling should occur on this operation
	his[14] = "fourteen"; 
	assert(his.size() == 17 && his.capacity() == 32); 

	return 0;
}
