cmake_minimum_required(VERSION 3.6)
project(graphlib)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=gnu++11")

set(SOURCE_FILES main.cpp src/node.cpp src/node.h src/graph.cpp src/graph.h)
add_executable(graphlib ${SOURCE_FILES} src/node.cpp src/node.h src/graph.cpp src/graph.h)