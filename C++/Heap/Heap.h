/*
 * Heap implementation 
 * The heap is represented internally as an array 
 *
 * To do this, consider each node to be indexed as an element in 
 * an array. Consider an index i. 
 * Children of the node will be at indexes (2i + 1) and (2i + 2)
 * The parent of the node is at floor((i-1)/2) 
 *
 *        0
 *       / \
 *      1   2 
 *     / \ / \
 *    3  4 5  6 
 * 
 * Take Node 2. Node 2's children are (2*2 + 1) = 5 and (2*2 + 2) = 6
 * Its parent is at (2-1)/2 = 0
 */ 

#ifndef HEAP_H
#define HEAP_H

#include <iostream> 
#include <stdexcept> 
#include <algorithm> 
#include <vector> 
#include <initializer_list> 

template <class T> 
class Heap {
public:
	Heap() {}
	Heap(std::initializer_list<T> list) : m_array(list) { heapsort(); }
	~Heap() {}

	/* Accessors */
	T getMax() const;
	int size() const; 
	bool empty() const; 
	int parent(int index) { return (index - 1) / 2; }
	int childOne(int index) { return 2 * index + 1; }
	int childTwo(int index) { return 2 * index + 2; }

	/* Mutators */ 
	void insert(T value); 
	void siftUp(int index);
	T extractMax(); 
	void siftDown(int index); 
	void remove(int index); 

	/* Algorithms */ 
	// void heapify(vector<T>& arr);
	void heapsort();

private:
	std::vector<T> m_array; 
};

template <class T> 
T Heap<T>::getMax() const {
	if (empty()) throw std::out_of_range("Cannot get max element of an empty heap"); 

	return m_array[0]; 
}

template <class T> 
int Heap<T>::size() const {
	return m_array.size(); 
}

template <class T> 
bool Heap<T>::empty() const {
	return m_array.size() == 0; 
}

template <class T> 
void Heap<T>::insert(T value) {
	m_array.push_back(value); 
	siftUp(size() - 1); 
}

template <class T> 
void Heap<T>::siftUp(int index) {
	while (index > 0) {
		if (m_array[parent(index)] < m_array[index]) 
			std::swap(m_array[parent(index)], m_array[index]);
		index = parent(index); 
	}
}

template <class T> 
T Heap<T>::extractMax() {
	if (empty()) throw std::out_of_range("Cannot extract from an empty heap"); 
	T ret = m_array[0]; 
	remove(0); 
	return ret; 
}

template <class T> 
void Heap<T>::siftDown(int index) {
	while (index <= parent(size())) {
		// Either two children or one children for current index 
		if (childTwo(index) < size()) {
			int tmp = (m_array[childOne(index)] > m_array[childTwo(index)]) ? childOne(index) : childTwo(index); 
			if (m_array[tmp] > m_array[index]) std::swap(m_array[tmp], m_array[index]); 
			index = tmp; 
		}
		else {
			if (m_array[childOne(index)] > m_array[index]) std::swap(m_array[childOne(index)], m_array[index]);
			index = childOne(index); 
		}
	}
}

template <class T> 
void Heap<T>::remove(int index) {
	if (empty()) throw std::out_of_range("Cannot remove from an empty heap"); 
	m_array[index] = m_array[size() - 1]; 
	m_array.pop_back(); 
	siftDown(index); 
}

template <class T> 
void Heap<T>::heapsort() {
	for (int i = size() - 1; i >= 0; --i) {
		siftUp(i); 
	}
}

#endif	// HEAP_H
