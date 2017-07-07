/**
 * Graph structure implemented with adjacency lists 
 * And several well-known graph algorithms 
 */

#include <iostream>
#include <fstream> 
#include <sstream>
#include <stack>
#include <queue> 
#include <climits>
#include <cassert> 
#include <algorithm> 
#include "Graph.h"
#include "../Heap/Heap.h" // for binary heap 

using namespace std; 

// Global variables used for DFS 
int start_time = 1;
int end_time = 1; 

/**
 * Graph constructor
 * @param file_name - path to file 
 * The file should be organized with the first line being the number the number of nodes 
 * The remaining lines should be edges of the form <node1> <node2> 
 * The edges are assumed to be directed
 */ 
Graph::Graph(string file_name) {
	int nodes; 
	string source, dest;
	string line; 
	ifstream file(file_name); 

	if (file.is_open()) {
		// Fetch the amount of nodes in the graph 
		getline(file, line); 
		nodes = stoi(line); 
		m_nodes = nodes; 
		m_adjacency_list.resize(nodes + 1);

		// Read the edges into the graph 
		while (getline(file, line)) {
			istringstream iss(line); 
			iss >> source >> dest; 
			addEdge(stoi(source), stoi(dest)); 
		}
	}
	else cout << "Unable to open file.";
}

vector<vector<int>> Graph::getAdjacencyList() {
	return m_adjacency_list; 
}

int Graph::getEdges() {
	return m_edges; 
}

int Graph::getNodes() {
	return m_nodes;
}

void Graph::addEdge(int source, int dest) {
	m_adjacency_list[source].push_back(dest);
}

/**
 * BFS 
 * @param start_node : node to start search from 
 * @return : vector of parent pointers, traces out BFS tree 
 * This BFS implementation assumes all nodes in the graph are connected 
 */ 
vector<int> Graph::BFS(int start_node) {
	// This array will keep track of each node's parents
	// -1 is the default and means no parent 
	// By the culmination of BFS, the parents array will 
	// trace out the BFS tree 
	vector<int> parents(m_nodes + 1, -1); 
	vector<int> seen(m_nodes + 1, 0); 

	queue<int> q; 
	q.push(start_node); 
	seen[start_node] = 1; 

	// Currently this assumes all nodes are connected 
	while (!q.empty()) {
		int current = q.front(); 
		q.pop(); 
		for (int next : m_adjacency_list[current]) {
			if (!seen[next]) {
				q.push(next); 
				parents[next] = current; 
				seen[next] = 1; 
			}
		}
	}
	return parents; 
}

/**
 * DFS 
 * @param start_node : node to start search from 
 * @return : vector of parent pointers, traces out DFS tree 
 * This is a recursive implementation that will visit all nodes 
 * even if not all nodes are connected 
 */ 
vector<int> Graph::DFS(int start_node) {
	// Resize start and end times array
	m_start_times.resize(m_nodes + 1, 0); 
	m_end_times.resize(m_nodes + 1, 0); 
	vector<int> parents(m_nodes + 1, -1); 
	vector<int> seen(m_nodes + 1, 0); 
	DFSHelper(start_node, parents, seen); 
	for (int i = 1; i < m_adjacency_list.size(); ++i)
		if (!seen[i]) DFSHelper(i, parents, seen);
	return parents; 
}

/**
 * DFSHelper
 * This is a recursive implementation 
 * Cycles are detected when an node is processed, but it has both 
 * 1) already been seen (via the seen vector) 
 * 2) is the parent of the node currently being recursed on 
 */ 
void Graph::DFSHelper(int start_node, vector<int>& parents, vector<int>& seen) {
	// Start time of node 
	seen[start_node] = 1; 
	m_start_times[start_node] = start_time++;
	for (int next : m_adjacency_list[start_node]) {
		if (!seen[next]) {
			parents[next] = start_node; 
			DFSHelper(next, parents, seen); 
		}
		else {
			// Back edge means cycle! 
			if (parents[start_node] != next) 
				cout << "Cycle found from " << start_node << " to " << next << endl;  
		}
	}
	// Finish time of node 
	m_end_times[start_node] = end_time++; 
}

/** 
 * DFSI - an iterative implementation of DFS 
 * @param start_node : node to start search from 
 * @return : vector of parent pointers, traces out DFS tree 
 * This is a recursive implementation that will visit all nodes 
 * even if not all nodes are connected 
 */ 
vector<int> Graph::DFSI(int start_node) {
	m_start_times.resize(m_nodes + 1, 0); 
	m_end_times.resize(m_nodes + 1, 0); 
	vector<int> parents(m_nodes + 1, -1); 
	vector<int> seen(m_nodes + 1, 0); 
	DFSIterative(start_node, parents, seen); 
	for (int i = 1; i < m_adjacency_list.size(); ++i)
		if (!seen[i]) DFSIterative(i, parents, seen); 
	return parents; 
}

/**
 * DFSIterative
 * This is a recursive implementation 
 * Cycles are detected when an node is processed, but it has both 
 * 1) already been seen (via the seen vector) 
 * 2) is the parent of the node currently being recursed on 
 * Because of the nature of the stack, this will actually process nodes 
 * in the reverse order of recursive DFS 
 */ 
void Graph::DFSIterative(int start_node, vector<int>& parents, vector<int>& seen) {
	stack<int> s; 
	s.push(start_node); 
	
	seen[start_node] = 1; 
	// Make sure we get all nodes 
	while (!s.empty()) {
		int current = s.top(); 
		s.pop(); 

		seen[current] = 1; 
		// m_start_times[current] = start_time++; 
		for (int next : m_adjacency_list[current]) {
			if (!seen[next]) {
				s.push(next); 
				parents[next] = current; 
			}
		}
		// m_end_times[current] = end_time++; 
	} 
}

// Helper function for BFS to recover node's distance from root 
int Graph::recoverDistance(vector<int> parents, int start_node) {
	int distance = 0; 
	while (start_node != -1) {
		start_node = parents[start_node]; 
		++distance; 
	}
}

vector<int> Graph::getStartTimes() {
	return m_start_times; 
}

vector<int> Graph::getEndTimes() {
	return m_end_times; 
}

//////////////////////////////////////////////////

/**
 * Weighted Graph Algorithms 
 */ 

WeightedGraph::WeightedGraph(string file_name) {
	int nodes; 
	string source, dest, weight; 
	string line; 
	ifstream file(file_name); 

	if (file.is_open()) {
		// Fetch the amount of nodes in the graph 
		getline(file, line); 
		nodes = stoi(line); 
		m_nodes = nodes; 
		m_adjacency_list.resize(nodes + 1);

		// Read the edges into the graph 
		while (getline(file, line)) {
			istringstream iss(line); 
			iss >> source >> dest >> weight; 
			addWeightedEdge(stoi(source), stoi(dest), stoi(weight)); 
		}
	}
	else cout << "Unable to open file.";
}

vector<vector<WeightedEdge>> WeightedGraph::getAdjacencyList() {
	return m_adjacency_list; 
}

int WeightedGraph::getEdges() {
	return m_edges; 
}

int WeightedGraph::getNodes() {
	return m_nodes; 
}

void WeightedGraph::addWeightedEdge(int source, int dest, int weight) {
	WeightedEdge tmp(source, dest, weight);
	m_adjacency_list[source].push_back(tmp); 
}

/**
 * Prims Algorithm
 * @param start_node : node to start algorithm from 
 * @return : a minimum spanning tree, retracable via parent pointers in the parent array 
 * 
 * Assumes all nodes are connected 
 * This is a naive algorithm that will run in quadratic time
 * A clever algorithm will use a priority queue, but needs to implement a 
 * hash map mapping values to indexes 
 */ 
vector<int> WeightedGraph::Prims(int start_node) {

	vector<int> parents(m_nodes + 1, -1); 
	vector<int> values(m_nodes + 1, INT_MAX); 
	vector<bool> inMST(m_nodes + 1, false); 

	// Start with the start_node
	values[start_node] = 0; 
	int total_cost = 0; 

	// This outer loop runs N times 
	// The inner two loops run a maximum of N times
	// yieling an asymptotic running time of O(N^2) 
	for (int count = 0; count < m_nodes; ++count) {
		// Search for the smallest edge to node not yet in MST
		int min = INT_MAX, num = -1; 
		for (int i = 0; i < values.size(); ++i) {
			if (!inMST[i] && values[i] < min) min = values[i], num = i; 
		}

		// Assuming we found our node
		if (num != -1) {
			inMST[num] = true; 
			total_cost += min; 
		}

		for (WeightedEdge w : m_adjacency_list[num]) {
			if (!inMST[w.dest] && w.weight < values[w.dest]) {
				parents[w.dest] = num; 
				values[w.dest] = w.weight; 
			}
		}
	}
	cout << "Total cost: " << total_cost << endl; 
	return parents; 
}

/**
 * Union-Find Data structure 
 * By cleverly using Union By Rank and Path Compression techniques
 * Finding the root element of a subset, and unifying two subsets can 
 * be made to run in O(log n) time 
 */ 

struct subset {
	int parent; 
	int rank; 
};

/** 
 * The root of a subset is found when the value in the subsets
 * array is the same as the node number 
 */
int find(vector<subset>& subsets, int i) {
	if (subsets[i].parent == i) 
		return i;
	return find(subsets, subsets[i].parent); 
}

/* 
 * CAREFUL, Union is a reserved keyword in C++
 */
void unionSet(vector<subset>& subsets, int s, int t) {
	int sroot = find(subsets, s); 
	int troot = find(subsets, t); 

	if (subsets[sroot].rank < subsets[troot].rank)
		subsets[sroot].parent = troot; 
	else if (subsets[troot].rank < subsets[sroot].rank)
		subsets[troot].parent = sroot; 
	else {
		// Equal ranks, arbitrarily assign one as the parent
		subsets[sroot].parent = troot; 
		subsets[troot].rank++; 
	}
}

/** 
 * Kruskal's Algorithm 
 * Assumes connected graph
 */

void WeightedGraph::Kruskals() {
	// Initialize Union-Find data structure 
	// Each node starts as the parent of itself 
	// with rank 0 
	vector<subset> subsets(m_nodes + 1); 
	for (int i = 0; i < subsets.size(); ++i) {
		subsets[i].parent = i; 
		subsets[i].rank = 0; 
	}

	// Sort the edges in the graph 
	// First, edges must be copied from adjacency list into edge vector
	vector<WeightedEdge> edges; 
	for (auto row : m_adjacency_list)
		for (WeightedEdge edge : row)
			edges.push_back(edge); 
	sort(edges.begin(), edges.end(), [](const WeightedEdge &x, const WeightedEdge& y) -> bool { return x.weight < y.weight; });

	int total_cost = 0; 
	// Process all edges in increasing order 
	// Add an edge only if does not form a cycle 
	// With Union-Find, a cycle is easily detected by discovering
	// if a candidate edge's vertices both have the same root 
	for (WeightedEdge edge: edges) {
		int sroot = find(subsets, edge.source);
		int droot = find(subsets, edge.dest); 
		if (sroot != droot) {
			unionSet(subsets, sroot, droot); 
			total_cost += edge.weight; 
			cout << "Added edge (" << edge.source << "," << edge.dest << ")" << endl;
		}
	}
	cout << "Total cost: " << total_cost << endl; 
}

/**
 * Dijkstra's Algorithm
 * Binary Heap does not need to implement decrease key necessarily 
 */ 
vector<int> WeightedGraph::Dijkstras(int start_node) {

}

