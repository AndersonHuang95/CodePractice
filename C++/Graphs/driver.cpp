#include "Graph.h"
#include <iostream> 

using namespace std; 

int main() {	
	Graph g("graph1.txt");
	// vector<int> p = g.BFS(3); 

	// cout << "Parent array for BFS: ";
	// for (int i = 1; i < p.size(); ++i)
	// 	cout << p[i] << " ";
	// cout << "\n";

	// cout << "Parent array for DFS: ";
	// vector<int> p2 = g.DFSI(3);
	// for (int i = 1; i < p2.size(); ++i)
	// 	cout << p2[i] << " "; 
	// cout << "\n"; 

	// cout << "Start times array for DFS: ";
	// for (int i = 1; i < p2.size(); ++i)
	// 	cout << g.getStartTimes()[i] << " ";
	// cout << "\n"; 

	// cout << "End times array for DFS: ";
	// for (int i = 1; i < p2.size(); ++i)
	// 	cout << g.getEndTimes()[i] << " ";
	// cout << "\n"; 

	WeightedGraph g3("graph3.txt");
	vector<int> p3 = g3.Prims(1); 
	for (int i = 1; i < p3.size(); ++i)
		cout << p3[i] << " "; 
	cout << "\n";
	
	return 0; 
}