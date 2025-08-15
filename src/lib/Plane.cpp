#include "Plane.h"

namespace IIIV {

Plane::Plane(double a, double b, double c, double d)
    : a_(a), b_(b), c_(c), d_(d) {}

double Plane::getA() const {
    return a_;
}

double Plane::getB() const {
    return b_;
}

double Plane::getC() const {
    return c_;
}

double Plane::getD() const {
    return d_;
}

} // namespace IIIV