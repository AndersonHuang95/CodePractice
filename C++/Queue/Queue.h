/* 
 * Queue implementations
 * Linked List and Array versions 
 */

#ifndef QUEUE_H
#define QUEUE_H

#include <stdexcept>
#include <iostream>
#include "../LinkedList/LinkedList.h"

#define DEFAULT_CAPACITY 16 

/* Queue implemented with Circular fixed-size array 
 * 
 *				DEFAULT_CAPACITY
 * <---------------------------------------->
 * 	  		  t	  h
 * ------------------------------------------
 *  |	|	|	|	|	|	|	|	|	|	|
 *-------------------------------------------
 * 
 * An empty queue starts with the head and tail indexes 
 * pointing to the same element
 * A full queue has the head and tail indexes pointing to adjacent 
 * elements such that (t + 1 % DEFAULT_CAPACITY) == h
 * Insertion occurs at the back (tail)
 * Removal occurs at the front (head) 
 */
template <class T> 
class Queue {
public:	
	Queue();
	~Queue() {}
	bool enqueue(T value); 
	void dequeue();
	void print() const; 
	T front() const; 
	T back() const; 
	int size() const; 
	bool empty() const; 
	bool full() const; 
private:
	T m_arr[DEFAULT_CAPACITY];
	int m_size;
	int m_front;  
	int m_back;
};

template <class T>
Queue<T>::Queue() : m_size(0) {
	m_front = 0;
	m_back = 0; 
}

/* No operation occurs if queue is full */
template <class T>
bool Queue<T>::enqueue(T value) {
	if (full()) {
		return false;
	}
	
	// Empty queue is a special case
	if (empty()) { 
		m_arr[m_front] = m_arr[m_back] = value; 
	}
	else {
		m_arr[m_back + 1 % DEFAULT_CAPACITY] = value; 
		m_back = (m_back + 1) % DEFAULT_CAPACITY; 
	}
	++m_size;
	return true; 
}

/* Exception thrown if popping empty queue */
template <class T> 
void Queue<T>::dequeue() {
	if (empty()) throw std::length_error("Empty queue cannot be popped"); 
	
	// No need to overwrite the front element
	// However, the queue may have one element, so move front and back 
	if (m_front == m_back) m_back = (m_back + 1) % DEFAULT_CAPACITY;  
	else m_front = (m_front + 1) % DEFAULT_CAPACITY; 
	--m_size; 
}

/* Debugging */
template <class T>
void Queue<T>::print() const {
	for (int i = 0; i < DEFAULT_CAPACITY; ++i) {
		std::cout << i << "\t\t";
	}
	std::cout << std::endl;
	for (int i = 0; i < DEFAULT_CAPACITY; ++i) {
		std::cout << m_arr[i] << "\t\t";
	}
	std::cout << std::endl;
}
template <class T>
T Queue<T>::front() const {
	return m_arr[m_front];
}

template <class T>
T Queue<T>::back() const {
	return m_arr[m_back]; 
}

template <class T>
int Queue<T>::size() const {
	return m_size; 
}

template <class T>
bool Queue<T>::empty() const {
	return (m_size ==  0); 
}

template <class T>
bool Queue<T>::full() const {
	return m_size == DEFAULT_CAPACITY; 
}	

/* 
 * Queue implemented with Linked List 
 * See LinkedList.h for details 
 *
 * To make insert and deletion operations cheap, 
 * the head is used for deletions and the tail
 * is used for insertions
 */
template <class T> 
class ListQueue {
public:
	ListQueue(); 
	~ListQueue(); 
	void enqueue(T value);
	void dequeue();
	T front() const;
	T back() const; 
	bool empty() const; 
private:
	LinkedList<T> m_list; 
};


template <class T>
ListQueue<T>::ListQueue() {}

template <class T>
ListQueue<T>::~ListQueue() {}

template <class T>
void ListQueue<T>::enqueue(T value) {
	// ListQueue has capacity dependent only on memory availability 
	m_list.push_back(value); 
}

template <class T>
void ListQueue<T>::dequeue() {
	if (m_list.empty()) throw std::length_error("Cannot pop an empty queue"); 
	m_list.pop_front(); 
}

template <class T>
T ListQueue<T>::front() const {
	return m_list.front(); 
}

template <class T>
T ListQueue<T>::back() const {
	return m_list.back(); 
}

template <class T>
bool ListQueue<T>::empty() const {
	return m_list.empty();
}

#endif // QUEUE_H
