#ifndef SORTS_H
#define SORTS_H

#include <vector> 
#include <algorithm> 

template <class T> 
void swap(T &a, T &b) {
	T tmp = a; 
	a = b;
	b = tmp; 
}

/****************************
 * Naive Sorts
 ****************************/

template <class T> 
void bubbleSort(std::vector<T>& arr) {
	int n = arr.size();
	for (int i = n - 1; i > 0; --i) {
		for (int j = 0; j < i; ++j) {
			if (arr[j] > arr[j + 1])
				swap(arr[j], arr[j + 1]); 
		}
	}
}

template <class T> 
void selectionSort(std::vector<T>& arr) {
	int n = arr.size(); 
	for (int i = 0; i < n - 1; ++i) {
		int smallest = i; 
		for (int j = i + 1; j < n; ++j) {
			if (arr[smallest] > arr[j])
				smallest = j;
		}
		swap(arr[i], arr[smallest]); 
	}
}

template <class T>
void insertionSort(std::vector<T>& arr) {
	int n = arr.size(); 
	for (int i = 1; i < n; ++i) {
		for (int j = i; j > 0; --j) {
			if (arr[j] < arr[j - 1])
				swap(arr[j], arr[j - 1]); 
		}
	}
}

/**********************
 * Merge Sort - Recursive
 * Merge sort is O(N Log N) worst and average case 
 * However, O(N) space is needed for an auxiliary array 
 **********************/
template <class T>
void merge(std::vector<T>& arr, std::vector<T>& aux, int low, int mid, int high) {
	// Copy arr to aux 
	for (int i = low; i <= high; ++i) 
		aux[i] = arr[i]; 
	int i = low, j = mid + 1; 
	for (int k = low; k <= high; ++k) {
		if (i > mid)	arr[k] = aux[j++];
		else if (j > high) arr[k] = aux[i++]; 
		else if (aux[i] <= aux[j]) arr[k] = aux[i++]; 
		else arr[k] = aux[j++]; 
	}
}

template <class T>
void sort(std::vector<T>& arr, std::vector<T>& aux, int low, int high) {
	if (high <= low) return; 
	int mid = low + (high - low) / 2; 
	sort(arr, aux, low, mid); 
	sort(arr, aux, mid + 1, high); 
	merge(arr, aux, low, mid, high);
}

template <class T>
void mergesort(std::vector<T>& arr) {
	// Declare an auxiliary array to house elements 
	std::vector<T> aux(arr.size()); 
	sort(arr, aux, 0, arr.size() - 1); 
}

/**********************
 * Quick Sort
 **********************/

template <class T> 
void sorthelper(std::vector<T>& arr, int low, int high) {
	if (high <= low) return; 
	int lt = low, gt = high;
	int v = arr[low]; 
	int i = low; 
	while (i <= gt) {
		if (arr[i] < v) swap(arr[lt++], arr[i++]);
		else if (arr[i] > v) swap(arr[i], arr[gt--]);
		else i++;
	}

	sorthelper(arr, low, lt - 1); 
	sorthelper(arr, gt + 1, high); 
}

template <class T> 
void quicksort(std::vector<T>& arr) {
	std::random_shuffle(arr.begin(), arr.end()); 
	sorthelper(arr, 0, arr.size() - 1); 
}
#endif // SORTS_H
