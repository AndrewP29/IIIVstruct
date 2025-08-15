#include <gtest/gtest.h>
#include "Face.h"
#include "Vertex.h"
#include "Plane.h"
#include <stdexcept>
#include <memory>

class FaceTest : public ::testing::Test {
protected:
    void SetUp() override {
        master_vertices = std::make_shared<std::vector<IIIV::Vertex>>();
        master_vertices->push_back({1,0,0}); // 0
        master_vertices->push_back({0,1,0}); // 1
        master_vertices->push_back({0,0,1}); // 2
        master_vertices->push_back({0,0,0}); // 3
    }

    std::shared_ptr<std::vector<IIIV::Vertex>> master_vertices;
};

TEST_F(FaceTest, CreationAndNormal) {
    std::vector<size_t> indices = {0, 1, 3};
    IIIV::Face face(master_vertices, indices);
    
    auto vertices = face.getVertices();
    ASSERT_EQ(vertices.size(), 3);
    EXPECT_EQ(vertices[0].getX(), 1);
    EXPECT_EQ(vertices[1].getY(), 1);
    EXPECT_EQ(vertices[2].getZ(), 0);

    const auto& normal = face.getNormal();
    EXPECT_EQ(normal.getX(), 0);
    EXPECT_EQ(normal.getY(), 0);
    EXPECT_EQ(normal.getZ(), 1);
}

TEST_F(FaceTest, ThrowsOnCollinearVertices) {
    master_vertices->push_back({2,0,0}); // 4
    std::vector<size_t> indices = {0, 4, 3}; // (1,0,0), (2,0,0), (0,0,0) -> Collinear
    ASSERT_THROW(IIIV::Face face(master_vertices, indices), std::invalid_argument);
}

TEST_F(FaceTest, PlaneEquation) {
    std::vector<size_t> indices = {0, 1, 2};
    IIIV::Face face(master_vertices, indices);
    IIIV::Plane plane = face.getPlaneEquation();
    // For vertices (1,0,0), (0,1,0), (0,0,1), the normal should be (1,1,1) and D should be -1
    EXPECT_NEAR(plane.getA(), 1, 1e-9);
    EXPECT_NEAR(plane.getB(), 1, 1e-9);
    EXPECT_NEAR(plane.getC(), 1, 1e-9);
    EXPECT_NEAR(plane.getD(), -1, 1e-9);
}

TEST_F(FaceTest, InvertMethodFlipsNormal) {
    std::vector<size_t> indices = {0, 1, 2}; // Original order
    IIIV::Face face(master_vertices, indices);
    IIIV::Vertex original_normal = face.getNormal();

    face.invert(); // Invert the face
    IIIV::Vertex inverted_normal = face.getNormal();

    // The inverted normal should be the negative of the original normal
    EXPECT_NEAR(inverted_normal.getX(), -original_normal.getX(), 1e-9);
    EXPECT_NEAR(inverted_normal.getY(), -original_normal.getY(), 1e-9);
    EXPECT_NEAR(inverted_normal.getZ(), -original_normal.getZ(), 1e-9);
}

TEST_F(FaceTest, VerticesLieOnPlane) {
    std::vector<size_t> indices = {0, 1, 2};
    IIIV::Face face(master_vertices, indices);
    IIIV::Plane plane = face.getPlaneEquation();

    for (const auto& v : face.getVertices()) {
        double result = plane.getA() * v.getX() + 
                        plane.getB() * v.getY() + 
                        plane.getC() * v.getZ() + 
                        plane.getD();
        EXPECT_NEAR(result, 0, 1e-9);
    }
}