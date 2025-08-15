#include "Solid.h"
#include <map>

namespace IIIV {

Solid::Solid(std::shared_ptr<std::vector<Vertex>> all_vertices, const std::vector<Face>& faces)
    : vertices_ptr_(all_vertices), faces_(faces) {}

const std::vector<Face>& Solid::getFaces() const {
    return faces_;
}

Solid Solid::project(const Plane& plane) const {
    std::shared_ptr<std::vector<IIIV::Vertex>> new_all_vertices = std::make_shared<std::vector<IIIV::Vertex>>();
    std::vector<Face> new_faces;
    std::map<size_t, size_t> old_to_new_vertex_map; // Map from original vertex index to new vertex index

    // First, collect all unique projected vertices and build the mapping
    for (const auto& face : faces_) {
        for (size_t original_vertex_index : face.getIndices()) {
            if (old_to_new_vertex_map.find(original_vertex_index) == old_to_new_vertex_map.end()) {
                // This vertex hasn't been projected yet
                const IIIV::Vertex& original_vertex = (*vertices_ptr_)[original_vertex_index];
                IIIV::Vertex projected_vertex = original_vertex.project(plane);
                new_all_vertices->push_back(projected_vertex);
                old_to_new_vertex_map[original_vertex_index] = new_all_vertices->size() - 1;
            }
        }
    }

    // Now, create the new faces using the new_all_vertices and the mapping
    for (const auto& face : faces_) {
        std::vector<size_t> new_face_indices;
        for (size_t original_vertex_index : face.getIndices()) {
            new_face_indices.push_back(old_to_new_vertex_map[original_vertex_index]);
        }
        new_faces.emplace_back(new_all_vertices, new_face_indices);
    }

    return Solid(new_all_vertices, new_faces);
}

Solid Solid::project() const {
    std::shared_ptr<std::vector<IIIV::Vertex>> new_all_vertices = std::make_shared<std::vector<IIIV::Vertex>>();
    std::vector<Face> new_faces;
    std::map<size_t, size_t> old_to_new_vertex_map; // Map from original vertex index to new vertex index

    // First, collect all unique projected vertices and build the mapping
    for (const auto& face : faces_) {
        for (size_t original_vertex_index : face.getIndices()) {
            if (old_to_new_vertex_map.find(original_vertex_index) == old_to_new_vertex_map.end()) {
                // This vertex hasn't been projected yet
                const IIIV::Vertex& original_vertex = (*vertices_ptr_)[original_vertex_index];
                IIIV::Vertex projected_vertex = original_vertex.project(); // Default project
                new_all_vertices->push_back(projected_vertex);
                old_to_new_vertex_map[original_vertex_index] = new_all_vertices->size() - 1;
            }
        }
    }

    // Now, create the new faces using the new_all_vertices and the mapping
    for (const auto& face : faces_) {
        std::vector<size_t> new_face_indices;
        for (size_t original_vertex_index : face.getIndices()) {
            new_face_indices.push_back(old_to_new_vertex_map[original_vertex_index]);
        }
        new_faces.emplace_back(new_all_vertices, new_face_indices);
    }

    return Solid(new_all_vertices, new_faces);
}

} // namespace IIIV
