#include "Vector.h"

namespace IIIV {

Vector::Vector(double x, double y, double z)
    : x_(x), y_(y), z_(z) {}

Vector::~Vector() {}

double Vector::getX() const {
    return x_;
}

double Vector::getY() const {
    return y_;
}

double Vector::getZ() const {
    return z_;
}

void Vector::setX(double x) {
    x_ = x;
}

void Vector::setY(double y) {
    y_ = y;
}

void Vector::setZ(double z) {
    z_ = z;
}

} // namespace IIIV
