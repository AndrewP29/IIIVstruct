#include "Vertex.h"
#include "Plane.h"
#include <cmath> // For std::sqrt

namespace IIIV {

Vertex::Vertex(double x, double y, double z)
    : x_(x), y_(y), z_(z) {}

Vertex::~Vertex() {}

double Vertex::getX() const {
    return x_;
}

double Vertex::getY() const {
    return y_;
}

double Vertex::getZ() const {
    return z_;
}

void Vertex::setX(double x) {
    x_ = x;
}

void Vertex::setY(double y) {
    y_ = y;
}

void Vertex::setZ(double z) {
    z_ = z;
}

Vertex Vertex::cross(const Vertex& other) const {
    return Vertex(
        y_ * other.z_ - z_ * other.y_,
        z_ * other.x_ - x_ * other.z_,
        x_ * other.y_ - y_ * other.x_
    );
}

Vertex Vertex::project(const Plane& plane) const {
    // Plane equation: Ax + By + Cz + D = 0
    // Normal vector of the plane: N = (A, B, C)
    // Point to project: P = (x_, y_, z_)

    // Calculate t = (Ax + By + Cz + D) / (A^2 + B^2 + C^2)
    double numerator = plane.getA() * x_ + plane.getB() * y_ + plane.getC() * z_ + plane.getD();
    double denominator = plane.getA() * plane.getA() + plane.getB() * plane.getB() + plane.getC() * plane.getC();

    // Handle the case where the denominator is zero (should not happen for a valid plane)
    if (denominator == 0.0) {
        // This implies A=B=C=0, which is not a valid plane normal. Return original point or throw error.
        // For now, return the original point as a fallback.
        return *this;
    }

    double t = numerator / denominator;

    // Projected point P' = P - tN
    double projected_x = x_ - t * plane.getA();
    double projected_y = y_ - t * plane.getB();
    double projected_z = z_ - t * plane.getC();

    return Vertex(projected_x, projected_y, projected_z);
}

Vertex Vertex::project() const {
    // Default to XY plane (z=0)
    return Vertex(x_, y_, 0.0);
}

} // namespace IIIV