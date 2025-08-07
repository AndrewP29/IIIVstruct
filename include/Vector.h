#ifndef VECTOR_H
#define VECTOR_H

namespace IIIV {

class Vector {
public:
    Vector(double x = 0.0, double y = 0.0, double z = 0.0);
    virtual ~Vector();

    double getX() const;
    double getY() const;
    double getZ() const;

    void setX(double x);
    void setY(double y);
    void setZ(double z);

    Vector cross(const Vector& other) const;

private:
    double x_, y_, z_;
};

} // namespace IIIV

#endif // VECTOR_H
