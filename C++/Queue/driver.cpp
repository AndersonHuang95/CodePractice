#include <cassert>
#include <iostream>
#include <string>
#include "Queue.h"

using namespace std; 

int main() {
	Queue<int> qi; 
	qi.enqueue(5); 
	qi.enqueue(4);
	qi.enqueue(3);
	qi.enqueue(2);
	qi.enqueue(1);

	assert(qi.front() == 5); 
	assert(qi.back() == 1); 
	assert(qi.size() == 5); 
	assert(!qi.empty() && !qi.full());
	
	qi.dequeue();
	assert(qi.front() == 4); 

	ListQueue<string> qs;
	qs.enqueue("First");
	qs.enqueue("In");
	qs.enqueue("First"); 
	qs.enqueue("Out"); 

	assert(qs.front() == "First" && qs.back() == "Out"); 

	qs.dequeue(); 
	assert(qs.front() == "In"); 
	
	return 0;
}
