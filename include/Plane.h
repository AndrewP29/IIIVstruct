/**
 * @file Plane.h
 * @brief Defines a plane in 3D space.
 */
#ifndef PLANE_H
#define PLANE_H

namespace IIIV {

class Plane {
public:
    Plane(double a, double b, double c, double d);

    double getA() const;
    double getB() const;
    double getC() const;
    double getD() const;

private:
    double a_, b_, c_, d_;
};

} // namespace IIIV

#endif // PLANE_H
