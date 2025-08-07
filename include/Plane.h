/**
 * @file Plane.h
 * @brief Defines a plane in 3D space.
 */
#ifndef PLANE_H
#define PLANE_H

#include "Vertex.h"

namespace IIIV {

/**
 * @struct Plane
 * @brief Represents a plane equation Ax + By + Cz + D = 0.
 */
struct Plane {
    Vertex normal; // Contains A, B, C
    double d;      // The D coefficient
};

} // namespace IIIV

#endif // PLANE_H
