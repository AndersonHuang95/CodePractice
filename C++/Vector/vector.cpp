/*
 * An implemntation of C++ Standard Template Libraary's Vector
 *
 * The class is defined as a template, so any valid data type Vector
 * can be defined
 */ 

#include <stdexcept> 
#include <string> 
#include "vector.h"

using namespace std; 

#define DEFAULT_CAPACITY 16

/* Default Constructor */
template <class T> 
Vector<T>::Vector() {
	m_capacity = DEFAULT_CAPACITY; 
	m_size = 0; 
	m_array = new T[DEFAULT_CAPACITY];
}

/* Custom constructor
 * capacity (int): desired capacity of vector
 */ 
template <class T>
Vector<T>::Vector(int capacity) {
	m_capacity = capacity; 
	m_size = 0; 
	m_array = new T[capacity]; 
}

/* Custom constructor, 
 * capacity (int): desired capacity of vector
 * value (T): value to set all elements to */
template <class T> 
Vector<T>::Vector(int capacity, T value) {
	m_capacity = capacity; 
	m_size = capacity;
	m_array = new T[capacity]; 
	for (int i = 0; i < m_capacity; ++i) {
		*(m_array + i) = value; 
	}
}

/* Destructor 
 * free dynamically allocated memory 
 */
template <class T> 
Vector<T>::~Vector() {	
	delete [] m_array; 
}

template <class T> 
int Vector<T>::size() const {
	return m_size; 
}

template <class T> 
int Vector<T>::capacity() const {
	return m_capacity; 
}

template <class T> 
bool Vector<T>::empty() const {
	return (m_size == 0); 
}

template <class T>
T Vector<T>::front() const {
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
T Vector<T>::back() const {
	if (empty()) {
		throw out_of_range("Out of bounds exception"); 
	}
	return *(m_array + m_size - 1); 
}

template <class T> 
T Vector<T>::at(int index) const {
	if (index >= m_size) {
		throw out_of_range("Index requested is greater than size"); 
	}
	return *(m_array + index); 
}

/* find 
 * Finds the index of the first occurrence of value in the Vector, -1 if not found
 * value (T): target value
 */
template <class T> 
int Vector<T>::find(T value) const {
	for (int i = 0; i < m_size; ++i) {
		if (*(m_array + i) == value) return i; 
	}
	return -1; 
}

/* []
 * square bracket operator offers random-access, like that for an array 
 */ 
template <class T>
T Vector<T>::operator[](int index) const {
	if (index >= m_size) {
		throw out_of_range("Out of bounds exception"); 
	}
	return *(m_array + index); 
}

/* push
 * Adds a value to the end of the vector
 * If the vector is at full capacity, the vector is resized (doubles in size) 
 */
template <class T> 
void Vector<T>::push_back(T value) {
	if (m_size == m_capacity) {
		resize(); 
	}
	
	*(m_array + m_size) = value; 
	++m_size; 
}

/* insert 
 * Inserts value at index, pushes all following values back 
 * index must be a non-negative integer, otherwise function does nothing 
 */ 
template <class T>
void Vector<T>::insert(int index, T value) {
	if (index < 0) return;

	if (m_size == m_capacity) {
		resize(); 
	}
	
	for (int i = m_size; i > index; --i) {
		*(m_array + i) = *(m_array + i - 1); 
	}

	*(m_array + index) = value;
	++m_size; 
}

/* prepend
 */ 
template <class T>
void Vector<T>::prepend(T value) {
	insert(0, value); 
}

/* pop_back
 * old value is not overwritten
 * only size is manipulated 
 */  
template <class T>
void Vector<T>::pop_back() {
	--m_size; 
}

/* erase
 * value at index is deleted and all elements
 * are shifted to the left
 * Index must be non-negative integer 
 */ 
template <class T> 
void Vector<T>::erase(int index) {
	if (index < 0) {
		throw out_of_range("Out of bounds exception"); 
	}

	for (int i = index; i < m_size - 1; ++i) {
		*(m_array + i) = *(m_array + i + 1); 
	}
	--m_size; 
}

/* remove
 * finds first occurrence of value and removes it from the vector
 * no action if value does not exist in the Vector 
 */ 
template <class T> 
void Vector<T>::remove(T value) {
	int index = find(value); 
	if (index != -1)
		erase(index); 
}

template <class T> 
void Vector<T>::resize() {
	// Copy over array elements
	m_capacity = m_capacity * 2; 
	delete [] m_array; 
	m_array = new T[m_capacity]; 
}

/* 
 * C++ feature: this cpp file and other files that may use Vector will be compiled separately
 * Files that use Vector will have the compiler implicity instantiate template classes of
 * certain types, but implementations of those member functions will not be in the object files
 * obtained from that compilation. In a similar manner, this cpp file will not have the specific
 * types of Vector instantiations needed in other files utilizing vector.cpp. 
 * THEREFORE, there are two solutions to the problem 
 * 1) At the end of class implementation files, such as this one, explicitly delineate what
 * template classes are required 
 * 
 * 2) Put the implementation of member functions in the header file that will be included
 * every time another module uses the template class
 *
 * For this module, I have decided to use Solution #1 
 * Soluton #2 may be a more flexible solution, but Solution #1 has a nice 
 * upside in that it prevents instantiations of template classes that have not 
 * been tested 
 */ 

template class Vector<int>;
template class Vector<double>;
template class Vector<string>; 
