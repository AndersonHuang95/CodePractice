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

// Enum for two-coloring 
// White & Black mark a node as seen 
// Gray means not yet seen 
enum color {
	WHITE, 
	BLACK, 
	GRAY, 
};

Graph::Graph(int size) {
	m_nodes = 0; 
	m_edges = 0; 
	m_adjacency_list.resize(size + 1); 
	m_connected_components = 1; 
}

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
		m_connected_components = 1; 
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

int Graph::getConnectedComponents() {
	return m_connected_components; 
}

void Graph::addEdge(int source, int dest) {
	m_adjacency_list[source].push_back(dest);
	m_edges++;
}

/**
 * BFS 
 * @param start_node : node to start search from 
 * @return : vector of parent pointers, traces out BFS tree 
 * This BFS implementation assumes all nodes in the graph are connected 
 * In the case of a disconnected graph, call this function within a 
 * wrapper function, that calls BFS on all nodes 
 * Time Complexity: O(E + V) 
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
 * Time Complexity: O(E + V) 
 */ 
vector<int> Graph::DFS(int start_node) {
	// Resize start and end times array
	int connected_components = 1; 
	vector<int> parents(m_nodes + 1, -1); 
	vector<int> seen(m_nodes + 1, 0); 
	DFSHelper(start_node, parents, seen); 
	for (int i = 1; i < m_adjacency_list.size(); ++i)
		if (!seen[i]) {
			DFSHelper(i, parents, seen);
			connected_components++; 
		}

	m_connected_components = connected_components;
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
	m_start_times.push_back(start_node); 
	for (int next : m_adjacency_list[start_node]) {
		if (!seen[next]) {
			parents[next] = start_node; 
			DFSHelper(next, parents, seen); 
		}
		else {
			// Back edge means cycle
			// For an undirected graph, an edge directly back to a node's parent
			// Does not mean a cycle, however 
			if (parents[start_node] != next) 
				; // cout << "Cycle found from " << start_node << " to " << next << endl;  
		}
	}
	// Finish time of node 
	m_end_times.push_back(start_node);  
}

/** 
 * DFSI - an iterative implementation of DFS 
 * @param start_node : node to start search from 
 * @return : vector of parent pointers, traces out DFS tree 
 * This is a recursive implementation that will visit all nodes 
 * even if not all nodes are connected 
 * Time Complexity: O(E + V) 
 */ 
vector<int> Graph::DFSI(int start_node) {
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
 * Because of the nature of iterative DFS, the parents array is not recorded 
 * correctly 
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

/**
 * recoverDistance
 * Helper function for BFS to recover node's distance from root 
 * @param parents : an array of parent pointers that retrace BFS tree
 * @param start_nodes : node whose distance is being queried 
 * return : distance (in # of edges) to root of BFS tree 
 */  
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

/**
 * These are basically DFS algorithms
 * Used to detect cycles in directed graphs 
 * A directed graph is distinct from a undirected graph 
 * To detect a cycle, we must keep track of a recursion stack which
 * delineates what nodes are currently being recursed on 
 * Another option would be to use start and end times, but that
 * method is more involved 
 */ 
bool Graph::hasCycle() {
	vector<int> rec_stack(m_nodes + 1, 0); 
	for (int i = 1; i < m_adjacency_list.size(); ++i) {
		vector<int> seen(m_nodes + 1, 0);
		if (!seen[i] && hasCycleHelper(i, rec_stack, seen)) return true; 
	}
	return false; 
}

bool Graph::hasCycleHelper(int start_node, vector<int>& rec_stack, vector<int>& seen) {
	// Start time of node 
	seen[start_node] = 1; 
	for (int next : m_adjacency_list[start_node]) {
		if (!seen[next]) {
			rec_stack[next] = 1; 
			return hasCycleHelper(next, rec_stack, seen); 
		}
		else if (rec_stack[next])
			return true; 
	}

	rec_stack[start_node] = 0; 
	return false; 
}

/** 
 * topologicalSort
 * @return : an array of vertices, in their order of visits 
 * return vector is empty if cycle exists
 */
vector<int> Graph::topologicalSort() {
	cout << m_edges << endl; 
	// Check for cycles 
	if (hasCycle()) {
		cout << "Cycle" << endl;
		return vector<int>(); 
	}
	// Time: O(V)
	// Preprocess the graph for in-edges
	vector<int> in_edges(m_nodes + 1, 0); 
	queue<int> q; 
	vector<int> ret; 
	for (vector<int> row : m_adjacency_list)
		for (int dest : row)
			in_edges[dest]++; 

	// Time: O(V)
	for (int i = 1; i < in_edges.size(); ++i) {
		if (in_edges[i] == 0) q.push(i); 
	}

	while (!q.empty()) {
		int current = q.front(); 
		ret.push_back(current); 
		q.pop(); 

		// Update the in_edges array 
		for (int dest : m_adjacency_list[current]) {
			in_edges[dest]--; 
			if (in_edges[dest] == 0) q.push(dest); 
		}
	}

	return ret; 
}

/* 
 * StronglyConnectedComponents 
 * @return : parents array that traces connected components s
 * Finds Strongly Connected Components 
 * Outputs the strongly connected components in a directed graph during construction
 * For future big fixes:
 * Note that when starting to loop from the end of an array, the index
 * should be one less than the array size ...
 */ 
vector<int> Graph::StronglyConnectedComponents() {
	// DFS to find finishing times 
	DFS(1); 

	// Reverse edges in graph 
	Graph reverse_graph(m_nodes); 
	for (int i = 1; i < m_adjacency_list.size(); ++i)
		for (int dest : m_adjacency_list[i])
			reverse_graph.addEdge(dest, i); 
	// TODO: Set nodes in reverse_graph to m_nodes 

	// Run DFS on reverse graph in reverse order of finishing time 
	int connected_components = 1; 
	vector<int> parents(m_nodes + 1, -1); 
	vector<int> seen(m_nodes + 1, 0); 
	for (int i = m_end_times.size() - 1; i >= 0; --i) {
		if (!seen[m_end_times[i]]) {
			cout << "In Strongly Connected Component " << m_end_times[i] << endl; 
			reverse_graph.DFSHelper(m_end_times[i], parents, seen);
			connected_components++; 
		}
	}
	return parents; 
}

/**
 * isBipartite
 * @return : boolean value that determines wehther or not graph is bipartite
 * Checking for bipartite graphs boils down to 
 * a two-coloring problem with BFS (or DFS) 
 */
bool Graph::isBipartite() {
	// Preprocess
	// Check for connectedness 
	assert(m_nodes != 0);

	// Instead of a seen aray, we have an enum array 
	// with 3 possible colorings 
	vector<int> parents(m_nodes + 1, -1); 
	vector<color> colors(m_nodes + 1, GRAY); 

	// Start coloring 
	// Arbitrarily start with white
	queue<int> q; 
	q.push(1); 
	colors[1] = WHITE; 

	while (!q.empty()) {
		int current = q.front(); 
		q.pop(); 
		for (int next : m_adjacency_list[current]) {
			if (colors[next] == GRAY) {
				q.push(next); 
				parents[next] = current; 
				colors[next] = (colors[current] == WHITE) ? BLACK : WHITE;
			}
			// A conflict in coloring has arisen 
			else if (colors[current] == colors[next])
				return false;
		}
	}
	// Manipulate parents array if needed
	return true; 
}
//////////////////////////////////////////////////

/**
 * Weighted Graph Algorithms 
 */ 

/** 
 * Constructor 
 * Compared to regular graph constructor, 
 * this constructor takes in a file format that has an extra weight field
 * so three fields in total 
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
	m_edges++; 
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
 * However, this approach is too involved and not implemented here 
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
 * The minimum spanning trees are outputted as the algorithm is run 
 * Retracing the parent tree is possible, but not as useful because 
 * the holistic tree is formed from broken, subtrees 
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

	// Time: O(E log E) = O(E log V) because E is at most V^2, but the log turns this into a constant
	// Sort the edges in the graph 
	// Ideally, an array of edges would already exist, but because
	// the adjacency list is stored in a vector of vectors, we need to manually create a flattened version
	// First, edges must be copied from adjacency list into edge vector
	vector<WeightedEdge> edges; 
	for (auto row : m_adjacency_list)
		for (WeightedEdge edge : row)
			edges.push_back(edge); 
	sort(edges.begin(), edges.end(), [](const WeightedEdge &x, const WeightedEdge& y) -> bool { return x.weight < y.weight; });

	int total_cost = 0; 

	// Time: O(E Log V) 
	// We examine all edges, with find and union operations taking at most O(log V) time
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
 * This again assumes a connected graph 
 * @param start_node : vertex to start single-source shortest path algorithm from
 * @return : a Dijkstra tree with parent pointers that trace nodes to their predecessors
 */ 
vector<int> WeightedGraph::Dijkstras(int start_node) {
	/* 
	 * Currently assumes connectneess 
	 * Check for connectedness here if needed
	 */ 

	// Comparator class for priority queue
	struct CompareEdge {
		bool operator()(const WeightedEdge& x, const WeightedEdge& y) {
			return x.weight > y.weight; 
		}
	};

	// Bookkeeping information to retrace tree, see which nodes
	// have been processed, and cheapest distances to unexamined nodes
	vector<int> parents(m_nodes + 1, -1); 
	vector<bool> seen(m_nodes + 1, false); 
	vector<int> distances(m_nodes + 1, INT_MAX); 
	priority_queue<WeightedEdge, vector<WeightedEdge>, CompareEdge> pq; 

	WeightedEdge w(start_node, start_node, 0);
	pq.push(w);  
	int nodes_processed = 0; 

	// Time: O(E log E)
	// This loop runs until all nodes have been processed
	// This implementation does not  overwrite elements in the priority queue
	// Still, each node will have at most (V - 1) connections
	// Accordingly, at most E edges will be examined. 
	// Restoring and managing the priority queue takes O(log E) per iteration
	while(nodes_processed < m_nodes) {
		WeightedEdge current = pq.top(); 
		pq.pop(); 

		// The edge is valid if we have not yet seen it 
		if (!seen[current.dest]) {
			seen[current.dest] = true; 
			distances[current.dest] = current.weight; 
			parents[current.dest] = current.source; 

			int distance = current.weight; 
			cout << "Current distance: " << distance << endl; 
			cout << "For edge " << current.dest << " adding:" << endl;
			// Add to heap lazily, deal with duplicates accordingly 
			for (WeightedEdge edge : m_adjacency_list[current.dest]) {
				WeightedEdge tmp(current.dest, edge.dest, distance + edge.weight);
				cout << "(" << current.dest << "," << edge.dest << ")" << " with weight " << distance + edge.weight << endl;
				pq.push(tmp); 
			}
			nodes_processed++; 
		}
	}

	return distances; 
}





