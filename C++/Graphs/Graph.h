/* 
 * Graph 
 */ 

#ifndef GRAPH_h
#define GRAPH_h

#include <vector> 
#include <string> 

class Graph {
public:
	Graph(std::string file_name); 

	/* Getters */ 
	std::vector<std::vector<int>> getAdjacencyList();
	int getEdges();
	int getNodes();

	/* Setters */ 
	void addEdge(int source, int dest); 

	/* Algorithms */ 
	vector<int> BFS(int start_node); 
	vector<int> DFS(int start_node); 
private: 
	std::vector<std::vector<int>> m_adjacency_list; 
	std::vector<int> m_start_times;
	std::vector<int> m_end_times; 
	int m_edges; 
	int m_nodes; 
};

#endif // GRAPH_H