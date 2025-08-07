/**
 * @file Face.h
 * @brief Defines a planar face composed of vertices from a shared list.
 */
#ifndef FACE_H
#define FACE_H

#include "Vertex.h"
#include "Plane.h"
#include <vector>
#include <memory>

namespace IIIV {

/**
 * @class Face
 * @brief Represents a planar face defined by indices into a shared vertex list.
 */
class Face {
public:
    /**
     * @brief Constructs a Face.
     * @param all_vertices A shared pointer to a vector of all vertices in the model.
     * @param vertex_indices A list of indices specifying which vertices from the master list form this face.
     */
    Face(std::shared_ptr<std::vector<IIIV::Vertex>> all_vertices, const std::vector<size_t>& vertex_indices);

    /**
     * @brief Gets the vertices that make up this face.
     * @return A vector of Vertex objects.
     */
    std::vector<IIIV::Vertex> getVertices() const;

    /**
     * @brief Gets the pre-calculated outward-facing normal of the face.
     * @return A const reference to the face's normal Vertex.
     */
    const IIIV::Vertex& getNormal() const;

    /**
     * @brief Gets the indices of the vertices that make up this face.
     * @return A const reference to the vector of vertex indices.
     */
    const std::vector<size_t>& getIndices() const;

    /**
     * @brief Inverts the face by reversing the order of its vertices, which flips its normal.
     */
    void invert();

    /**
     * @brief Calculates the plane equation (Ax + By + Cz + D = 0) for the face.
     * @return A Plane object representing the equation.
     */
    Plane getPlaneEquation() const;

private:
    std::shared_ptr<std::vector<IIIV::Vertex>> vertices_ptr_;
    std::vector<size_t> indices_;
    IIIV::Vertex normal_;

    /**
     * @brief Calculates and updates the face's normal vector.
     */
    void calculateNormal();
};

} // namespace IIIV

#endif // FACE_H
