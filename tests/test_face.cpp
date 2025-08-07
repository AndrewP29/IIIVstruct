#include <gtest/gtest.h>
#include "Face.h"
#include "Vector.h"
#include "Plane.h"
#include <stdexcept>

TEST(FaceTest, Creation) {
    std::vector<IIIV::Vector> vertices = {{1,0,0}, {0,1,0}, {0,0,1}};
    ASSERT_NO_THROW(IIIV::Face face(vertices));
}

TEST(FaceTest, ThrowsOnCollinearVertices) {
    std::vector<IIIV::Vector> vertices = {{1,1,1}, {2,2,2}, {3,3,3}};
    ASSERT_THROW(IIIV::Face face(vertices), std::invalid_argument);
}

TEST(FaceTest, PlaneEquation) {
    std::vector<IIIV::Vector> vertices = {{1,0,0}, {0,1,0}, {0,0,0}};
    IIIV::Face face(vertices);
    IIIV::Plane plane = face.getPlaneEquation();
    // Normal vector should be (0, 0, 1) for a face on the XY plane
    EXPECT_EQ(plane.normal.getX(), 0);
    EXPECT_EQ(plane.normal.getY(), 0);
    EXPECT_EQ(plane.normal.getZ(), 1);
    // Plane passes through origin, so D should be 0
    EXPECT_EQ(plane.d, 0);
}

TEST(FaceTest, VerticesLieOnPlane) {
    std::vector<IIIV::Vector> vertices = {{1,2,3}, {4,5,6}, {7,8,10}};
    IIIV::Face face(vertices);
    IIIV::Plane plane = face.getPlaneEquation();

    for (const auto& v : face.getVertices()) {
        double result = plane.normal.getX() * v.getX() + 
                        plane.normal.getY() * v.getY() + 
                        plane.normal.getZ() * v.getZ() + 
                        plane.d;
        EXPECT_NEAR(result, 0, 1e-9);
    }
}