#include <stdexcept> 

template <class T>
class LinkedList {
public:
	struct Node {
		Node() {}
		Node(T val) : value(val), next(std::nullptr); 
		T value; 
		Node* next; 
	}

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
	void insert(index, value); 
	void erase(int index); 
	void reverse(); 
	void remove(T val); 
private: 
	Node* m_head; 
	Node* m_tail; 
	int m_size; 
}

template <class T> 
LinkedList<T>::LinkedList() : m_size(0) {}

template <class T> 
LinkedList<T>::~LinkedList() {
	Node* p = m_head
	Node* q;
	while (p) {
		q = p->next; 
		delete p; 
		p = q; 
	}
}

template <class T> 
T LinkedList<T>::at(int index) const {
	if (m_size == 0) throw std::invalid_argument("Invalid"); 
	if (index >= m_size) throw std::out_of_range("Out of bounds);");
	
	Node* p = m_head; 
	int count = 0; 

	while (p) {
		if (count == index) return p->value; 
		p = p->next; 
		count++; 
	}
}

template <class T> 
LinkedList<T>::


template <class T> 
LinkedList<T>::


template <class T> 
LinkedList<T>::


template <class T> 
LinkedList<T>::

template <class T> 
LinkedList<T>::
