/*
 * An implemntation of C++ Standard Template Libraary's Vector
 *
 * The class is defined as a template, so any valid data type Vector
 * can be defined
 */ 

#ifndef VECTOR_H
#define VECTOR_H

template <class T>
class Vector {
public: 
	/* Default Constructor */
	Vector();

	/* Custom constructors */ 
	Vector(int capacity);
	Vector(int capacity, T value); 
	
	/* Assignment and Copy Constructors would go here 
	 * Should override them, because assigning private 
	 * vector pointer would be incorrect behavior
	 */ 
	
	/* Destructor 
	 * Should be virtual if it is a base class 
	 * virtual assures that the destructor process starts at the top instead of the middle */ 
	~Vector();

	/* Member Functions */

	/* Accessors - Const functions means they won't modify member variables 
	 * NOT the same as declaring a variable to be const */ 
	int size() const;
	int capacity() const; 
	bool empty() const;
	T front() const; 
	T back() const; 
	T at(int index) const;
	int find(T value) const;
	T operator[](int index) const;  


	/* Mutators */ 
	void push_back(T value); 
	void insert(int index, T value); 
	void prepend(T value); 
	void pop_back(); 
	void erase(int index); 
	void remove(T value); 
	
private:
	T* m_array;	// Pointer to the vector 
	int m_capacity; 
	int m_size; // Current size of the vector 
	void resize(); 
};

#endif /* VECTOR_H */
