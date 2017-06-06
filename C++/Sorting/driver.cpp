#include <iostream> 
#include <random>
#include <functional> 
#include <algorithm>
#include <cassert>
#include "sorts.h"

using namespace std; 

void print(vector<int>& arr) {
	for (int i = 0; i < arr.size(); ++i) {
		cout << arr[i] << "\t"; 
	}
	cout << "\n"; 
}

bool isSorted(vector<int>& arr) {
	for (int i = 1; i < arr.size(); ++i) 
		if (arr[i] < arr[i - 1]) return false; 
	return true; 
}
int main() {
	// vector<int> a = {10, 3, 2, 6, 3, 8, 1, 5, 4};
	// vector<int> b = {7, 6, 11, 2, 4, 8, 9, 1, 13}; 
	// vector<int> c = {15, 25, 3, 6, 1, 10, 23, 10}; 

	// cout << "Unsorted: "; 
	// print(a);
	// bubbleSort(a); 
	// cout << "Sorted: "; 
	// print(a); 

	// cout << "Unsorted: "; 
	// print(b);
	// selectionSort(b); 
	// cout << "Sorted: "; 
	// print(b); 

	// cout << "Unsorted: "; 
	// print(c); 
	// insertionSort(c); 
	// cout << "Sorted: "; 
	// print(c);

	random_device rnd_device; 
	mt19937 mersenne_engine(rnd_device()); 
	uniform_int_distribution<int> dist(1, 100); 
	auto gen = std::bind(dist, mersenne_engine); 
	vector<int> vec(10000000); 
	generate(vec.begin(), vec.end(), gen); 

	quicksort(vec); 
	assert(isSorted(vec)); 

	return 0;
}
