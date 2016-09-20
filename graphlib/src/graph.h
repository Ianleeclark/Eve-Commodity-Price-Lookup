//
// Created by ilcia on 9/10/2016.
//

#ifndef GRAPHLIB_GRAPH_H
#define GRAPHLIB_GRAPH_H

#include "node.h"

class Graph {
public:
    Graph(std::string);
    void add_node(Node);
    void print_nodes() const;
private:
    // TODO(ian): I'd like to have an LRU cache here to speed up lookups.

    // TODO(ian): Should we allow a blank graph object
    Graph();
    std::vector<Node> known_nodes;
};

#endif //GRAPHLIB_GRAPH_H
