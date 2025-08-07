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
