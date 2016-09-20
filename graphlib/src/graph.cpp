//
// Created by ilcia on 9/10/2016.
//

#include "graph.h"
#include "node.h"

#include <fstream>
#include <iostream>
#include <iterator>
#include <sstream>
#include <algorithm>

static std::vector<std::string>
split_string(std::string line) {
    std::stringstream ss(line);
    ss.str();

    std::string item;
    std::vector<std::string> out = {};
    while(std::getline(ss, item, ',')) {
        out.push_back(item);
    }

    return out;
}

static Node
create_node(std::string line) {
    /*
     * Handles parsing a CSV of node location data.
     */

    // TODO(ian): This should do error handling and throw an exception if
    // invalid line is parsed.
    std::vector<std::string> items = split_string(line);

    Node node = Node(static_cast<const size_t>(atoi(items[0].c_str())), items[1]);

    return node;
}

void
Graph::add_node(Node node) {
    known_nodes.push_back(node);
}

void Graph::print_nodes() const {
    for(auto node: known_nodes) {
        std::cout << node.get_id() << "=" << node.title << std::endl;
    }
}

Graph::Graph(std::string file_name) {
    std::ifstream infile;
    infile.open(file_name);

    std::string file_data = "0,Jita\n1,Amarr";
    std::istringstream iss(file_data);

    std::vector<std::string> locations{
            std::istream_iterator<std::string>{iss},
            std::istream_iterator<std::string>{}
    };

    for(auto location : locations) {
        this->add_node(create_node(location));
    }
}
