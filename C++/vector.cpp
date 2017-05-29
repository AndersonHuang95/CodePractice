/*
 * An implemntation of C++ Standard Template Libraary's Vector
 *
 * The class is defined as a template, so any valid data type Vector
 * can be defined
 */ 

#include <iostream>
#include <vector.h>
#include <stdexcept> 

using namespace std; 

#DEFINE DEFAULT_CAPACITY 16

/* Default Constructor */
template <class T> 
Vector::Vector() {
	m_capacity = DEFAULT_CAPACITY; 
	m_size = 0; 
	m_array = new T[DEFAULT_CAPACITY];
}

/* Custom constructor
 * capacity (int): desired capacity of vector
 */ 
template <class T>
Vector::Vector(int capacity) {
	m_capacity = capacity; 
	m_size = 0; 
	m_array = new T[capacity]; 
}

/* Custom constructor, 
 * capacity (int): desired capacity of vector
 * value (T): value to set all elements to */
template <class T> 
Vector::Vector(int capacity, T value) {
	m_capacity = capacity; 
	m_size = capacity;
	m_array = new T[capacity]; 
	for (int i = 0; i < m_capacity; ++i) {
		T[i] = value; 
	}
}

/* Destructor 
 * free dynamically allocated memory 
 */
Vector::~Vector() {	
	delete [] m_array; 
}

int Vector::size() const {
	return m_size; 
}

int Vector::capacity() const {
	return m_capacity; 
}

bool Vector::empty() const {
	return (m_size == 0); 
}

template <class T>
T Vector::front() const {
	/* this keyword is implicit, compiler knows to call Vector's member function
	 * If there was a function with the same name in global scope, you could use
	 * :: to resolve that function instead 
	 */ 
	if (empty()) {
		throw out_of_range("Out of bounds exception"); 
	}
	return *m_array; 
}

template <class T> 
T Vector::back() const {
	if (empty()) {
		throw out_of_range("Out of bounds exception"); 
	}
	return *(m_array + size - 1); 
}

template <class T> 
T Vector::at(int index) const {
	if (index >= size) {
		throw out_of_range("Index requested is greater than size"); 
	}
	return *(m_array + index); 
}

/* find 
 * Finds the index of the first occurrence of value in the Vector, -1 if not found
 * value (T): target value
 */
int Vector::find(T value) const {
	for (int i = 0; i < size(); ++i) {
		if (*(m_array + i) == value) return i; 
	}
	return -1; 
}

// Driver program
int main() {

}
