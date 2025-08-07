/**
 * @file Face.h
 * @brief Defines a planar face composed of 3D vertices.
 */
#ifndef FACE_H
#define FACE_H

#include "Plane.h"

#include "Vector.h"
#include <vector>

namespace IIIV {

/**
 * @class Face
 * @brief Represents a planar face defined by a set of vertices.
 */
class Face {
public:
    /**
     * @brief Constructs a Face from a list of vertices.
     * @param vertices A vector of shared pointers to Vector objects.
     */
    Face(const std::vector<Vector>& vertices);

    /**
     * @brief Gets the vertices of the face.
     * @return A const reference to the vector of vertices.
     */
    const std::vector<Vector>& getVertices() const;

    /**
     * @brief Calculates the plane equation (Ax + By + Cz + D = 0) for the face.
     * @return A Plane object representing the equation.
     */
    Plane getPlaneEquation() const;

private:
    std::vector<Vector> vertices_;
};

} // namespace IIIV

#endif // FACE_H
