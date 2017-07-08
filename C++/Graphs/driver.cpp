#include "Graph.h"
#include <iostream> 
#include <cassert> 

using namespace std; 

int main() {	
	Graph g("test/graph1.txt");
	vector<int> p = g.BFS(3); 

	cout << "Parent array for BFS: \n";
	for (int i = 1; i < p.size(); ++i)
		cout << p[i] << " ";
	cout << "\n";

	// cout << "Parent array for DFS: \n";
	// vector<int> p2 = g.DFS(3);
	// for (int i = 1; i < p2.size(); ++i)
	// 	cout << p2[i] << " "; 
	// cout << "\n"; 

	// cout << "Start times array for DFS: \n";
	// for (int i = 1; i < p2.size(); ++i)
	// 	cout << g.getStartTimes()[i] << " ";
	// cout << "\n"; 

	// cout << "End times array for DFS: \n";
	// for (int i = 1; i < p2.size(); ++i)
	// 	cout << g.getEndTimes()[i] << " ";
	// cout << "\n"; 

	Graph g2("test/graph2.txt"); 
	vector<int> t = g2.topologicalSort(); 

	cout << "Order of nodes for topological sort: \n";
	for (int i = 0; i < t.size(); ++i)
		cout << t[i] << " ";
	cout << "\n"; 

	WeightedGraph g3("test/graph3.txt");
	vector<int> p3 = g3.Prims(1); 
	for (int i = 1; i < p3.size(); ++i)
		cout << p3[i] << " "; 
	cout << "\n";

	g3.Kruskals(); 

	WeightedGraph g4("test/graph4.txt"); 
	vector<int> d = g4.Dijkstras(1); 
	for (int i = 1; i < d.size(); ++i) 
		cout << d[i] << " "; 
	cout << "\n";

	Graph g5("test/graph5.txt"); 
	g5.DFS(1);
	assert(g5.getConnectedComponents() == 3);

	Graph g6("test/graph6.txt"); 
	g6.StronglyConnectedComponents(); 

	Graph g7("test/graph7.txt");
	assert(g7.isBipartite()); 

	Graph g8("test/graph8.txt");
	assert(!g8.isBipartite()); 

	return 0; 
}