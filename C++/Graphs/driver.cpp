#include "Graph.h"

using namespace std; 

int main() {
	Graph g("graph1.txt")
	vector<int> p = g.BFS(); 
	for (int i = 1; i < p.size(); ++i)
		cout << p[i]; 

	return 0; 
}