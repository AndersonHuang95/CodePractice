#include <iostream>
#include <cassert>
#include "Heap.h"

using namespace std;

int main() {
	Heap<int> hi; 
	hi.insert(3);
	hi.insert(1); 
	hi.insert(2);
	hi.insert(7);
	hi.insert(8);
	hi.insert(5);
	hi.insert(4);
	
	assert(hi.getMax() == 8); 
	hi.extractMax(); 
	assert(hi.getMax() == 7); 
	
	/* O(n) to create the heap */ 
	Heap<double> hd = {1.0, 2.0, 3.0, 4.0, 5.0, 7.0, 8.0}; 

	/* O(n log n) to create the sorted array in place 
	 * because ceil(n/2) nodes are leaves */
	hd.heapsort(); 
	for (int i = 0; i < hd.size(); ++i) 
		cout << hd.getHeap()[i] << " "; 
	cout << endl; 

}
