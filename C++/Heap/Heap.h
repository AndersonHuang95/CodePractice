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
	Heap(std::initializer_list<T> list) : m_array(list) { heapify(); }
	~Heap() {}

	/* Accessors */
	T getMax() const;
	int size() const; 
	bool empty() const; 
	int parent(int index) const { return (index - 1) / 2; }
	int childOne(int index) const { return 2 * index + 1; }
	int childTwo(int index) const { return 2 * index + 2; }
	std::vector<T> getHeap() const { return m_array; } 
	
	/* Mutators */ 
	void insert(T value); 
	void siftUp(int index);
	T extractMax(); 
	void siftDown(int index, int size); 
	void remove(int index); 

	/* Algorithms */ 
	void heapify();
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
void Heap<T>::siftDown(int index, int size) {
	int largest = index; 
	int l = childOne(index);
	int r = childTwo(index);

	if (l < size && m_array[l] > m_array[largest]) largest = l;
	if (r < size && m_array[r] > m_array[largest]) largest = r; 
	if (largest != index) {
		std::swap(m_array[index], m_array[largest]); 
		siftDown(size, largest);
	}
	/*
	while (index <= parent(size)) {
		// Either two children or one children for current index 
		if (childTwo(index) < size) {
			int tmp = (m_array[childOne(index)] > m_array[childTwo(index)]) ? childOne(index) : childTwo(index); 
			if (m_array[tmp] > m_array[index]) std::swap(m_array[tmp], m_array[index]); 
			index = tmp; 
		}
		else {
			if (m_array[childOne(index)] > m_array[index]) std::swap(m_array[childOne(index)], m_array[index]);
			index = childOne(index); 
		}
	}
	*/
}

template <class T> 
void Heap<T>::remove(int index) {
	if (empty()) throw std::out_of_range("Cannot remove from an empty heap"); 
	std::swap(m_array[index], m_array[size() - 1]);  
	m_array.pop_back(); 
	siftDown(index, size()); 
}

template <class T> 
void Heap<T>::heapify() {
	for (int i = size(); i >= 0; --i) {
		siftUp(i); 
	}
}

/* In-place sort */ 
template <class T>
void Heap<T>::heapsort() {
	for (int i = size() - 1; i >= 0; --i) {
		//std::cout << i << "\t" << m_array[0] << "\t" << m_array[i] << "\t"; 
		//for (int j = 0; j < size(); j++) 
		//	std::cout << m_array[j] << " ";
		//std::cout << std::endl; 
		std::swap(m_array[0], m_array[i]);
		siftDown(0, i);  
	}
}
#endif	// HEAP_H
