/* 
 * Hash Table
 * A take on C++'s unordered_map 
 * This implementation rehashes whenever the number of items, n,
 * exceeds the number of buckets, m
 * 
 * Recall that the expression (n/m) is the load factor of a hash table
 * The amortized cost of insertion is O(1 + n/m) = O(1) if (n/m) is a constant 
 * The expected cost of insertion and search is O(1) 
 * 
 * This implementation uses linear probing 
 */

 #ifndef HASHTABLE_H
 #define HASHTABLE_H

#include <stdexcept> 
#include <functional> // for built-in hash function
#include <iostream> 

#define INITIAL_SIZE 16

enum states_t {
	UNUSED = 0,
	USED = 1, 
	REMOVED = 2
};


/* 
 * S is the data type of the key 
 * T is the data type of the value 
 */
template <class S, class T> 
class HashTable {
public:	
	struct KeyValue {		
		S first; 
		T second; 
	};

	/* Constructor and Destructor */
	HashTable();
	~HashTable(); 

	/* Accessors */
	/* Note these functions cannot call functions that are not const as well */
	bool exists(S key) const; 
	T get(S key) const; 
	T& operator[](S key) const; 
	int size() const; 
	int capacity() const; 

	/* Mutators */
	void add(S key, T value); 
	void remove(S key); 
private:
	void resize(); 
	int hash(S key) const;
	std::hash<S> m_hash; // May not be defined for custom classes 
	
	/* It seems there is no special feature in C++
	 * To check if a variable has been assigned
	 * Therefore, I have made two separate arrays in memory 
	 * to represent the hash table. 
	 * m_table handles the actual data
	 * m_intialized serves to determine if a slot has been used, unused or removed
	 * 0 :- unused
	 : 1 :- used
	 : 2 :- removed
	 */
	KeyValue *m_table; 
	states_t *m_initialized; 
	int m_buckets; 
	int m_items; 
};

template <class S, class T>
HashTable<S,T>::HashTable() {
	m_table = new KeyValue[INITIAL_SIZE]; 
	m_initialized = new states_t[INITIAL_SIZE]; 
	m_buckets = INITIAL_SIZE; 
	m_items = 0; 
	
	// Assign sentinel values to table slots
	for (int i = 0; i < m_buckets; ++i) {
		m_initialized[i] = UNUSED; 
	}
}

template <class S, class T> 
HashTable<S,T>::~HashTable() {
	delete [] m_table;
	delete [] m_initialized;
}

/* Probing the table requires care 
 * Slots that are marked with REMOVED signify 
 * that linear probing should continue until
 * a slot that is UNUSED is found, or we have 
 * completely exhausted the table 
 */
template <class S, class T> 
bool HashTable<S,T>::exists(S key) const {
	// Linear probe, may end up going around
	// the end of the array and into the beginning

	int index = hash(key) % m_buckets;
	if (m_initialized[index] == USED && m_table[index].first == key) return true;

	for (int i = index + 1; i != index; i = (i + 1) % m_buckets) {
		if (m_initialized[i] == USED && m_table[i].first == key) return true; 
		else if (m_initialized[i] == UNUSED) return false;
		else ; // slot is REMOVED, keep looping
	}
	return false; 
}

template <class S, class T> 
T HashTable<S,T>::get(S key) const{
	int index = hash(key) % m_buckets; 
	if (m_initialized[index] == USED && m_table[index].first == key) 
		return m_table[index].second;

	for (int i = index + 1; i != index; i = (i + 1) % m_buckets) {
		if (m_initialized[i] == USED && m_table[i].first == key) 
			return m_table[i].second;
		else if (m_initialized[i] == UNUSED)
			throw std::out_of_range("Key does not exist"); 
		else ; // slot is REMOVED, keep searching	
	}
	throw std::out_of_range("Key does not exist"); 
}

/* Opposed to get, this function will not error out 
 * if the key is not present 
 * This function will mark a slot as marked even if 
 * all is done is access the element, without assigning it a value
 */
template <class S, class T> 
T& HashTable<S,T>::operator[](S key) const {
	int index = hash(key) % m_buckets; 
	if (m_initialized[index] == USED && m_table[index].first == key) 
		return m_table[index].second; 

	for (int i = index + 1; i != index; i = (i + 1) % m_buckets) {
		if (m_initialized[i] == USED && m_table[i].first == key) 
			return m_table[i].second;
		else if (m_initialized[i] == UNUSED) {
			return m_table[index].second;
		}
		else ; // slot is REMOVED, keep searching	
	}
}

template <class S, class T> 
int HashTable<S,T>::size() const {
	return m_items; 
}

template <class S, class T> 
int HashTable<S,T>::capacity() const {
	return m_buckets; 
}
/* Overwrites value if key already exists */
template <class S, class T>
void HashTable<S,T>::add(S key, T value) {
	// Check if the key is unique 
	if (!exists(key)) {
		// Check if table is full
		if (m_items == m_buckets) 
			resize();

		int index = hash(key) % m_buckets; 
		for (int i = index + 1; i != index; i = (i + 1) % m_buckets) {
			if (m_initialized[index] != USED) {
				m_initialized[index] = USED; 
				m_table[index].first = key; 
				m_table[index].second = value; 
			}	
		}
		++m_items; 
	}
	// Otherwise, overwrite - no need to modify m_initialized or # items
	else {
		int index = hash(key) % m_buckets; 
		for (int i = index + 1; i != index; i = (i + 1) % m_buckets) {
			if (m_initialized[index] != USED) { 
				m_table[index].first = key; 
				m_table[index].second = value; 
			}
		}
	}
}

template <class S, class T> 
void HashTable<S,T>::remove(S key) {
	// Values are not overwritten
	// instead, the enum value is changed in m_initialized 
	m_initialized[hash(key) % m_buckets] = REMOVED; 
	--m_items; 
}

template <class S, class T>
void HashTable<S,T>::resize() {
	// Table doubling
	int new_size = m_buckets * 2;
	KeyValue *tmp = new KeyValue[new_size];
	states_t *s = new states_t[new_size]; 

	// O(n) to initialize 1
	for (int i = 0; i < new_size; ++i) {
		s[i] = UNUSED; 
	}

	// O(n) to copy over elements
	// Must probe entirety of original table
	for (int i = 0; i < m_buckets; ++i) {
		// This is an extra check, not needed for linear probing
		if (m_initialized[i] == USED) {
			int new_index = hash(m_table[i].first) % new_size;  
			tmp[new_index] = m_table[i]; 
			s[new_index] = USED; 
		}
	}

	// Set new data members
	m_buckets = new_size; 
	m_table = tmp;
	m_initialized = s; 
}

template <class S, class T>
int HashTable<S,T>::hash(S key) const{
	return m_hash(key); 
}

#endif // HASHTABLE_H
