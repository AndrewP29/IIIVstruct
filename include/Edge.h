/**
 * @file Edge.h
 * @brief Defines an edge by its two vertex indices.
 */
#ifndef EDGE_H
#define EDGE_H

#include <cstddef> // For size_t
#include <utility> // For std::pair

namespace IIIV {

/**
 * @struct Edge
 * @brief Represents an undirected edge between two vertices.
 *        The indices are always stored in sorted order (v1 < v2) to ensure uniqueness.
 */
struct Edge {
    size_t v1;
    size_t v2;

    // Constructor to ensure v1 < v2
    Edge(size_t p1, size_t p2) {
        if (p1 < p2) {
            v1 = p1;
            v2 = p2;
        } else {
            v1 = p2;
            v2 = p1;
        }
    }

    // For use in std::map or std::set
    bool operator<(const Edge& other) const {
        if (v1 != other.v1) {
            return v1 < other.v1;
        }
        return v2 < other.v2;
    }
};

} // namespace IIIV

#endif // EDGE_H
