/* 
 * Graph 
 */ 

#ifndef GRAPH_h
#define GRAPH_h

#include <vector> 
#include <string> 

struct WeightedEdge {
	WeightedEdge(int s, int d, int w) : source(s), dest(d), weight(w) { }
	int source; 
	int dest; 
	int weight; 
};

class Graph {
public:
	Graph(std::string file_name); 

	/* Getters */ 
	std::vector<std::vector<int>> getAdjacencyList();
	int getEdges();
	int getNodes();
	std::vector<int> getStartTimes(); 
	std::vector<int> getEndTimes();
	
	/* Setters */ 
	void addEdge(int source, int dest); 

	/* Algorithms */ 
	std::vector<int> BFS(int start_node); 
	std::vector<int> DFS(int start_node); 
	std::vector<int> DFSI(int start_node);

	void DFSIterative(int start_node, std::vector<int>& parents, std::vector<int>& seen);
	void DFSHelper(int start_node, std::vector<int>& parents, std::vector<int>& seen);
	int recoverDistance(std::vector<int> parents, int start_node);
private: 
	std::vector<std::vector<int>> m_adjacency_list;
	std::vector<int> m_start_times;
	std::vector<int> m_end_times; 
	int m_edges; 
	int m_nodes; 
};

class WeightedGraph {
public: 
	WeightedGraph(std::string file_name); 

	/* Getters */ 
	std::vector<std::vector<WeightedEdge>> getAdjacencyList();
	int getEdges();
	int getNodes();

	/* Setters */ 
	void addWeightedEdge(int source, int dest, int weight); 

	/* Algorithms */ 
	std::vector<int> Prims(int start_node); 
	void Kruskals(); 
	std::vector<int> Dijkstras(int start_node); 
private: 
	std::vector<std::vector<WeightedEdge>> m_adjacency_list;
	int m_edges; 
	int m_nodes; 
};

#endif // GRAPH_H