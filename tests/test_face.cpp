#include "Face.h"
#include "Plane.h"
#include <cassert>
#include <iostream>
#include <stdexcept>
#include <cmath>

void test_face_creation() {
    std::vector<IIIV::Vector> vertices = {
        {1.0, 0.0, 0.0},
        {0.0, 1.0, 0.0},
        {0.0, 0.0, 1.0}
    };
    IIIV::Face face(vertices);
    assert(face.getVertices().size() == 3);
    std::cout << "test_face_creation passed." << std::endl;
}

void test_plane_equation() {
    std::vector<IIIV::Vector> vertices = {
        {1.0, 0.0, 0.0},
        {0.0, 1.0, 0.0},
        {0.0, 0.0, 0.0}
    };
    IIIV::Face face(vertices);
    IIIV::Plane plane = face.getPlaneEquation();
    assert(plane.normal.getX() == 0);
    assert(plane.normal.getY() == 0);
    assert(plane.normal.getZ() == 1);
    assert(plane.d == 0);
    std::cout << "test_plane_equation passed." << std::endl;
}

void test_vertices_on_plane() {
    std::vector<IIIV::Vector> vertices = {
        {2.0, 3.0, 4.0},
        {1.0, 5.0, 2.0},
        {3.0, 1.0, 6.0}
    };
    IIIV::Face face(vertices);
    IIIV::Plane plane = face.getPlaneEquation();

    for (const auto& v : face.getVertices()) {
        double result = plane.normal.getX() * v.getX() + 
                        plane.normal.getY() * v.getY() + 
                        plane.normal.getZ() * v.getZ() + 
                        plane.d;
        assert(std::abs(result) < 1e-9);
    }
    std::cout << "test_vertices_on_plane passed." << std::endl;
}

void test_collinear_exception() {
    std::vector<IIIV::Vector> vertices = {
        {1.0, 0.0, 0.0},
        {2.0, 0.0, 0.0},
        {3.0, 0.0, 0.0}
    };
    IIIV::Face face(vertices);
    try {
        face.getPlaneEquation();
        assert(false); // Should not reach here
    } catch (const std::runtime_error& e) {
        assert(std::string(e.what()) == "Vertices are collinear, cannot form a plane.");
        std::cout << "test_collinear_exception passed." << std::endl;
    }
}

int main() {
    test_face_creation();
    test_plane_equation();
    test_vertices_on_plane();
    test_collinear_exception();
    return 0;
}
