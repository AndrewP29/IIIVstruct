#ifndef VERTEX_H
#define VERTEX_H

namespace IIIV {

class Vertex {
public:
    Vertex(double x = 0.0, double y = 0.0, double z = 0.0);
    virtual ~Vertex();

    double getX() const;
    double getY() const;
    double getZ() const;

    void setX(double x);
    void setY(double y);
    void setZ(double z);

    Vertex cross(const Vertex& other) const;

private:
    double x_, y_, z_;
};

} // namespace IIIV

#endif // VERTEX_H