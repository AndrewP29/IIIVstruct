#include <gtest/gtest.h>
#include "Vertex.h"

TEST(VertexTest, ConstructorAndGetters) {
    IIIV::Vertex v(1.0, 2.0, 3.0);
    EXPECT_EQ(v.getX(), 1.0);
    EXPECT_EQ(v.getY(), 2.0);
    EXPECT_EQ(v.getZ(), 3.0);
}

TEST(VertexTest, Setters) {
    IIIV::Vertex v;
    v.setX(4.0);
    v.setY(5.0);
    v.setZ(6.0);
    EXPECT_EQ(v.getX(), 4.0);
    EXPECT_EQ(v.getY(), 5.0);
    EXPECT_EQ(v.getZ(), 6.0);
}

TEST(VertexTest, CrossProduct) {
    IIIV::Vertex v1(1.0, 0.0, 0.0);
    IIIV::Vertex v2(0.0, 1.0, 0.0);
    IIIV::Vertex cross = v1.cross(v2);
    EXPECT_EQ(cross.getX(), 0.0);
    EXPECT_EQ(cross.getY(), 0.0);
    EXPECT_EQ(cross.getZ(), 1.0);
}

TEST(VertexTest, ProjectMethod) {
    IIIV::Vertex v(1.0, 2.0, 3.0);

    // Test default projection (onto XY plane, z=0)
    IIIV::Vertex projected_default = v.project();
    EXPECT_NEAR(projected_default.getX(), 1.0, 1e-9);
    EXPECT_NEAR(projected_default.getY(), 2.0, 1e-9);
    EXPECT_NEAR(projected_default.getZ(), 0.0, 1e-9);

    // Test projection onto a custom plane (e.g., XZ plane, y=0)
    IIIV::Plane xz_plane(0.0, 1.0, 0.0, 0.0); // Normal (0,1,0), D=0
    IIIV::Vertex projected_xz = v.project(xz_plane);
    EXPECT_NEAR(projected_xz.getX(), 1.0, 1e-9);
    EXPECT_NEAR(projected_xz.getY(), 0.0, 1e-9);
    EXPECT_NEAR(projected_xz.getZ(), 3.0, 1e-9);

    // Test projection onto a plane with offset (e.g., z=5)
    IIIV::Plane z_offset_plane(0.0, 0.0, 1.0, -5.0); // Normal (0,0,1), D=-5 (z-5=0 => z=5)
    IIIV::Vertex projected_z_offset = v.project(z_offset_plane);
    EXPECT_NEAR(projected_z_offset.getX(), 1.0, 1e-9);
    EXPECT_NEAR(projected_z_offset.getY(), 2.0, 1e-9);
    EXPECT_NEAR(projected_z_offset.getZ(), 5.0, 1e-9);
}
