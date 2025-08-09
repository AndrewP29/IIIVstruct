/**
 * @file Solid.h
 * @brief Defines a solid object composed of faces.
 */
#ifndef SOLID_H
#define SOLID_H

#include "Vertex.h"
#include "Face.h"
#include <vector>
#include <memory>

namespace IIIV {

/**
 * @class Solid
 * @brief Represents a 3D solid object defined by a collection of faces and a shared vertex list.
 */
class Solid {
public:
    /**
     * @brief Constructs a Solid object.
     * @param all_vertices A shared pointer to the master list of vertices.
     * @param faces A vector of Face objects that compose the solid.
     */
    Solid(std::shared_ptr<std::vector<Vertex>> all_vertices, const std::vector<Face>& faces);

    /**
     * @brief Checks if the solid is closed (manifold).
     *        A solid is closed if every edge is shared by exactly two faces.
     * @return True if the solid is closed, false otherwise.
     */
    const std::vector<Face>& getFaces() const;

private:
    std::shared_ptr<std::vector<Vertex>> vertices_ptr_;
    std::vector<Face> faces_;
};

} // namespace IIIV

#endif // SOLID_H
