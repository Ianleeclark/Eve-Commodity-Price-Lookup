//
// Created by ilcia on 9/9/2016.
//

#include "node.h"

#include <algorithm>

static std::pair<int, Node>
new_node_pair(const Node x) {
    return std::pair<int, Node>(x.get_id(), x);
};

Node::Node(const size_t id, const std::string title) {
    this->id = id;
    this->title = title;
}

Node::Node(const size_t id, const std::vector<Node> neighbors) {
    for(auto itr = neighbors.begin(), end = neighbors.end(); itr != end; itr++) {
        this->neighbors.insert(new_node_pair(*itr));
    }
}

size_t
Node::get_id() const {
    return id;
}

void
Node::add_neighbor(const Node neighbor) {
    neighbors.insert(new_node_pair(neighbor));
}
