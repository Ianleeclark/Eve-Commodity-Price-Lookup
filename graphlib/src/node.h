//
// Created by ilcia on 9/9/2016.
//

#ifndef GRAPHLIB_NODE_H
#define GRAPHLIB_NODE_H

#include <map>
#include <vector>

using std::map;

class Node {
public:
    size_t id;
    std::string title;

    Node(const size_t, const std::string);
    // Create a list with variable neighbors.
    Node(const size_t, const std::vector<Node>);

    size_t get_id() const;
    void add_neighbor(const Node);
private:
    // `visited` indicates if a node has been visited whilst
    // traversing the graph.
    bool visited;

    std::map<const int, const Node> neighbors;
    // We don't ever want a `Node` initiated without an ID.
    // Moreover, we want to explicitly control which node has
    // which ID, so assigning one randomly is a poor choice.
    // As such, we'll just leave this blank and never implemented.
    Node();
};

#endif //GRAPHLIB_NODE_H
