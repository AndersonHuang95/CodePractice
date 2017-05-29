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
	void insert(int index, T value); 
	void erase(int index); 
	void reverse(); 
	void remove(T value); 
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
}

void template <class T> 
LinkedList<T>::pop_back() {
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
}

template <class T> 
T LinkedList<T>::front() {
	if (m_size == 0) throw std::out_of_range("Out of bounds"); 
	return m_head->value; 
}

template <class T>
T LinkedList<T>::back() {
	if (m_size == 0) throw std::out_of_range("Out of bounds"); 
	return m_tail->value; 
}

template <class T>
void LinkedList<T>::insert(int index, T value) {
	if (index < 0) throw std::invalid_argument("Bad parameter passed"); 
	if (index >= m_size) throw std::out_of_range("Out of bounds"); 

	if (index == m_size - 1) {
		push_back(); 
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
			}
			return;
		}
		q = p;
		p = p->next; 
		++count;
	}
}

template <class T>
LinkedList<T>::reverse() {
	m_tail = m_head; 
	Node* prev = nullptr;
	NOde* current = m_head; 
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
LinkedList<T>::remove(T value) {
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
			}
			return;
		}
		q = p;
		p = p->next; 
		++count;
	}
}
