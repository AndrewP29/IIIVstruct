#include "Vertex.h"

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

} // namespace IIIV