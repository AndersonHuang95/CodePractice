#include <iostream>
#include <fstream> 
#include <sstream>
#include <queue> 
#include "Graph.h"

using namespace std; 

Graph::Graph(string file_name) {
	int nodes; 
	int source, dest; 
	string line; 
	ifstream file(file_name); 

	if (file.is_open()) {
		// Fetch the amount of nodes in the graph 
		getline(file, line); 
		nodes = stoi(line); 
		m_adjacency_list.resize(nodes + 1);

		// Read the edges into the graph 
		while (getline(file, line)) {
			istringstream iss(line); 
			line >> source >> dest; 
			addEdge(source, dest); 
		}
	}
	else cout << "Unable to open file."
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

vector<int> BFS(int start_node) {
	// This array will keep track of each node's parents
	// -1 is the default and means no parent 
	// By the culmination of BFS, the parents array will 
	// trace out the BFS tree 
	vector<int> parents(m_nodes + 1, -1); 

	queue<int> q; 
	q.push(start_node); 

	// Currently this assumes all ndoes are connected 
	while (!q.empty()) {
		int current = q.front(); 
		q.pop(); 
		for (int i = 0; i < m_adjacency_list[current].size(); ++i) {
			int next = m_adjacency_list[current][i];
			// Only add a node to the queue if it has not been explored 
			if (parents[next] == -1) {
				q.push(next); 
				parents[next] = current; 
			}
		}
	}
	return parents; 
}