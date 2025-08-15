#include "Face.h"
#include <stdexcept>
#include <algorithm>

namespace IIIV {

Face::Face(std::shared_ptr<std::vector<IIIV::Vertex>> all_vertices, const std::vector<size_t>& vertex_indices)
    : vertices_ptr_(all_vertices), indices_(vertex_indices) {
    
    if (indices_.size() < 3) {
        throw std::invalid_argument("A face must have at least 3 vertex indices.");
    }

    // Check for duplicate indices among the first three vertices
    if (indices_[0] == indices_[1] || indices_[0] == indices_[2] || indices_[1] == indices_[2]) {
        throw std::invalid_argument("First three vertices of a face must be unique.");
    }

    calculateNormal();
}

std::vector<IIIV::Vertex> Face::getVertices() const {
    std::vector<IIIV::Vertex> face_vertices;
    face_vertices.reserve(indices_.size());
    for (size_t index : indices_) {
        face_vertices.push_back((*vertices_ptr_)[index]);
    }
    return face_vertices;
}

const IIIV::Vertex& Face::getNormal() const {
    return normal_;
}

const std::vector<size_t>& Face::getIndices() const {
    return indices_;
}

void Face::invert() {
    std::reverse(indices_.begin(), indices_.end());
    calculateNormal(); // Recalculate normal after reversing indices
}

void Face::calculateNormal() {
    // Calculate normal and check for collinearity upon construction
    const IIIV::Vertex& p1 = (*vertices_ptr_)[indices_[0]];
    const IIIV::Vertex& p2 = (*vertices_ptr_)[indices_[1]];
    const IIIV::Vertex& p3 = (*vertices_ptr_)[indices_[2]];

    IIIV::Vertex v1(p2.getX() - p1.getX(), p2.getY() - p1.getY(), p2.getZ() - p1.getZ());
    IIIV::Vertex v2(p3.getX() - p1.getX(), p3.getY() - p1.getY(), p3.getZ() - p1.getZ());

    normal_ = v1.cross(v2);

    const double EPSILON = 1e-9;
    if (std::abs(normal_.getX()) < EPSILON &&
        std::abs(normal_.getY()) < EPSILON &&
        std::abs(normal_.getZ()) < EPSILON) {
        throw std::invalid_argument("Vertices are collinear, cannot form a plane.");
    }
}

Plane Face::getPlaneEquation() const {
    const IIIV::Vertex& p1 = (*vertices_ptr_)[indices_[0]];
    double d_val = - (normal_.getX() * p1.getX() + normal_.getY() * p1.getY() + normal_.getZ() * p1.getZ());
    return {normal_.getX(), normal_.getY(), normal_.getZ(), d_val};
}

Face Face::project(const Plane& plane) const {
    std::shared_ptr<std::vector<IIIV::Vertex>> projected_all_vertices = std::make_shared<std::vector<IIIV::Vertex>>();
    std::vector<size_t> projected_indices;
    projected_indices.reserve(indices_.size());

    for (size_t i = 0; i < indices_.size(); ++i) {
        const IIIV::Vertex& original_vertex = (*vertices_ptr_)[indices_[i]];
        IIIV::Vertex projected_vertex = original_vertex.project(plane);
        projected_all_vertices->push_back(projected_vertex);
        projected_indices.push_back(i); // Indices into the new projected_all_vertices vector
    }

    return Face(projected_all_vertices, projected_indices);
}

Face Face::project() const {
    std::shared_ptr<std::vector<IIIV::Vertex>> projected_all_vertices = std::make_shared<std::vector<IIIV::Vertex>>();
    std::vector<size_t> projected_indices;
    projected_indices.reserve(indices_.size());

    for (size_t i = 0; i < indices_.size(); ++i) {
        const IIIV::Vertex& original_vertex = (*vertices_ptr_)[indices_[i]];
        IIIV::Vertex projected_vertex = original_vertex.project(); // Call the default project for Vertex
        projected_all_vertices->push_back(projected_vertex);
        projected_indices.push_back(i); // Indices into the new projected_all_vertices vector
    }

    return Face(projected_all_vertices, projected_indices);
}

} // namespace IIIV
