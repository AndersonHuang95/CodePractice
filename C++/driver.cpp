#include <iostream>
#include <string>
#include <cassert> 
#include "vector.h"

using namespace std; 

// Driver program 
int main() {
	Vector<int> vi; 
	assert(vi.empty()); 
	Vector<double> vd(25); 
	assert(vd.size() == 0 && vd.capacity() == 25); 

	Vector<string> vs(16, "hello"); 
	assert(vs.size() == 16 && vs.capacity() == 16); 
	assert(vs.front() == "hello" && vs.back() == "hello"); 
	assert(vs.at(5) == "hello"); 
	
	vi.push_back(1); 
	vi.push_back(3); 
	vi.push_back(5);
	vi.push_back(7); 
	vi.push_back(9); 

	assert(vi.find(5) == 2); 
	assert(vi[4] == 9); 

	vi.insert(1, 2); 
	vi.prepend(0); 
	assert(vi.size() == 7); 

	vi.pop_back(); 
	assert(vi.size() == 6); 

	vi.erase(0); 
	assert(vi.size() == 5); 

	vi.remove(3); 
	assert(vi.size() == 4); 

	vi.remove(3); 
	assert(vi.size() == 4); 
	
	return 0; 
}
