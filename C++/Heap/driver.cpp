#include <iostream>
#include <cassert>
#include "Heap.h"

using namespace std;

bool lessthan(int& x, int& y) {
	return x < y; 
}

bool lessthan(double& x, double& y) {
	return x < y;
}

int main() {
	Heap<int> hi(lessthan); 
	for(int i = 25; i >= 0; --i) {
		hi.insert(i); 
	}
	
	assert(hi.getMax() == 25); 
	hi.extractMax(); 
	assert(hi.getMax() == 24); 
	
	hi.heapsort(); 
	for (int i = 0; i < hi.size(); ++i) 
		cout << hi.getHeap()[i] << " "; 
	cout << endl; 

}
