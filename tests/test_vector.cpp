#include <gtest/gtest.h>
#include "Vector.h"

TEST(VectorTest, ConstructorAndGetters) {
    IIIV::Vector v(1.0, 2.0, 3.0);
    EXPECT_EQ(v.getX(), 1.0);
    EXPECT_EQ(v.getY(), 2.0);
    EXPECT_EQ(v.getZ(), 3.0);
}

TEST(VectorTest, Setters) {
    IIIV::Vector v;
    v.setX(4.0);
    v.setY(5.0);
    v.setZ(6.0);
    EXPECT_EQ(v.getX(), 4.0);
    EXPECT_EQ(v.getY(), 5.0);
    EXPECT_EQ(v.getZ(), 6.0);
}

TEST(VectorTest, CrossProduct) {
    IIIV::Vector v1(1.0, 0.0, 0.0);
    IIIV::Vector v2(0.0, 1.0, 0.0);
    IIIV::Vector cross = v1.cross(v2);
    EXPECT_EQ(cross.getX(), 0.0);
    EXPECT_EQ(cross.getY(), 0.0);
    EXPECT_EQ(cross.getZ(), 1.0);
}