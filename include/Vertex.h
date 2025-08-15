#ifndef VERTEX_H
#define VERTEX_H

#include "Plane.h" // Added this line back

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

    /**
     * @brief Projects the vertex onto a given plane. If no plane is provided, projects onto the XY plane (z=0).
     * @param plane The plane to project onto.
     * @return A new Vertex object representing the projected point.
     */
    Vertex project(const Plane& plane) const;
    Vertex project() const;

private:
    double x_, y_, z_;
};

} // namespace IIIV

#endif // VERTEX_H