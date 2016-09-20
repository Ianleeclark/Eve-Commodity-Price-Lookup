#include <iostream>

#include "src/node.h"
#include "src/graph.h"

int main() {
    std::vector<Node> node_list;

    const Graph graph = Graph("test.txt");
    graph.print_nodes();

    std::cout << "Hello, World!" << std::endl;
    return 0;
}