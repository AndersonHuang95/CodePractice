/*
 * Linked List implementation
 */ 

#ifndef LINKEDLIST_H
#define LINKEDLIST_H

#include <stdexcept> 
#include <string>

template <class T>
class LinkedList {
public:
	struct Node {
		Node() {}
		Node(T val) : value(val), next(nullptr) {}
		T value; 
		Node* next; 
	};

	LinkedList(); 
	~LinkedList(); 

	int size() const; 
	bool empty() const;
	T at(int index) const; 
	void push_front(T value); 
	void pop_front(); 
	void push_back(T value);
	void pop_back();
	T front() const; 
	T back() const; 
	void insert(int index, T value); 
	void erase(int index); 
	void reverse(); 
	void remove(T value); 
private: 
	Node* m_head; 
	Node* m_tail; 
	int m_size; 
};

template <class T> 
LinkedList<T>::LinkedList() : m_size(0) {}

template <class T> 
LinkedList<T>::~LinkedList() {
	Node* p = m_head;
	Node* q;
	while (p) {
		q = p->next; 
		delete p; 
		p = q; 
	}
}

template <class T>
int LinkedList<T>::size() const {
	return m_size; 
}

template <class T>
bool LinkedList<T>::empty() const {
	return m_size == 0; 
}

template <class T> 
T LinkedList<T>::at(int index) const {
	if (m_size == 0) throw std::invalid_argument("Invalid"); 
	if (index >= m_size) throw std::out_of_range("Out of bounds");
	
	Node* p = m_head; 
	int count = 0; 

	while (p) {
		if (count == index) return p->value; 
		p = p->next; 
		count++; 
	}
}

template <class T> 
void LinkedList<T>::push_front(T value) {
	Node* tmp = new Node(value); 
	if (m_size == 0) {
		m_head = m_tail = tmp; 
	}	
	else {
		tmp->next = m_head; 
		m_head = tmp; 
	}
	++m_size;
}

template <class T> 
void LinkedList<T>::pop_front() {
	if (m_size == 0) throw std::out_of_range("Out of bounds");
	else if (m_size == 1) {
		delete m_head; 
		m_head = m_tail = nullptr;
	}
	else {
		Node* p = m_head->next; 
		delete m_head; 
		m_head = p; 
	}
	--m_size;
}

template <class T> 
void LinkedList<T>::push_back(T value) {
	Node*tmp = new Node(value); 
	if (m_size == 0) {
		m_head = m_tail = tmp;
	}
	else {
		m_head->next = tmp; 
		m_tail = tmp; 
	}
	++m_size;
}

template <class T> 
void LinkedList<T>::pop_back() {
	if (m_size == 0) throw std::out_of_range("Out of bounds"); 
	else if (m_size == 1) {
		delete m_tail;
		m_head = m_tail = nullptr; 
	}
	else {
		Node* p = m_head; 
		Node* q; 

		while(p && p->next != m_tail) {
			q = p; 
			p = p->next; 
		}

		q->next = nullptr; 
		delete p;
	}
	--m_size;
}

template <class T> 
T LinkedList<T>::front() const {
	if (m_size == 0) throw std::out_of_range("Out of bounds"); 
	return m_head->value; 
}

template <class T>
T LinkedList<T>::back() const {
	if (m_size == 0) throw std::out_of_range("Out of bounds"); 
	return m_tail->value; 
}

template <class T>
void LinkedList<T>::insert(int index, T value) {
	if (index < 0) throw std::invalid_argument("Bad parameter passed"); 
	if (index >= m_size) throw std::out_of_range("Out of bounds"); 

	if (index == m_size - 1) {
		push_back(value); 
		return;
	}

	Node* p = m_head; 
	Node* q = nullptr; 
	int count = 0; 

	while (p) {
		if (index == count) { 
			if (q == nullptr) {
				push_front(value); 
			}
			else {
				Node *tmp = new Node(value); 
				tmp->next = p; 
				q->next = tmp; 
				++m_size;
			}
			return;
		}
		q = p; 
		p = p->next; 
		++count; 
	}
}

template <class T> 
void LinkedList<T>::erase(int index) {
	if (index < 0) throw std::invalid_argument("Bad parameters passed"); 
	if (index >= m_size) throw std::out_of_range("Out of bounds"); 

	if (index == m_size - 1) {
		pop_back(); 
		return;
	}

	Node* p = m_head; 
	Node* q = nullptr; 
	int count = 0; 

	while (p) {
		if (index == count) {
			if (q == nullptr) {
				pop_front();
			}
			else {
				q->next = p->next; 
				delete p;
				--m_size;
			}
			return;
		}
		q = p;
		p = p->next; 
		++count;
	}
}

template <class T>
void LinkedList<T>::reverse() {
	m_tail = m_head; 
	Node* prev = nullptr;
	Node* current = m_head; 
	Node* next; 

	while (current) {
		next = current->next; 
		current->next = prev; 
		current = next; 
		prev = current;
	}

	m_head = prev; 
}

template <class T> 
void LinkedList<T>::remove(T value) {
	Node* p = m_head; 
	Node* q = nullptr; 
	
	while (p) {
		if (p->value == value) {
			if (q == nullptr) {
				pop_front(); 
			}
			else if (p == m_tail) {
				pop_back(); 
			}
			else {
				q->next = p->next; 
				delete p;
				--m_size;
			}
			return;
		}
		q = p;
		p = p->next; 
	}
}

#endif // LINKEDLIST_H
