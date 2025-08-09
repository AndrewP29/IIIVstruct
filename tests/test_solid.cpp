#include <gtest/gtest.h>
#include "Solid.h"
#include "Face.h"
#include "Vertex.h"
#include <memory>

class SolidTest : public ::testing::Test {
protected:
    void SetUp() override {
        master_vertices = std::make_shared<std::vector<IIIV::Vertex>>();
        // Vertices for a simple cube
        master_vertices->push_back({0,0,0}); // 0
        master_vertices->push_back({1,0,0}); // 1
        master_vertices->push_back({1,1,0}); // 2
        master_vertices->push_back({0,1,0}); // 3
        master_vertices->push_back({0,0,1}); // 4
        master_vertices->push_back({1,0,1}); // 5
        master_vertices->push_back({1,1,1}); // 6
        master_vertices->push_back({0,1,1}); // 7
    }

    std::shared_ptr<std::vector<IIIV::Vertex>> master_vertices;
};

TEST_F(SolidTest, Creation) {
    std::vector<IIIV::Face> faces;

    // Front face (0,1,2,3)
    faces.emplace_back(master_vertices, std::vector<size_t>{0, 1, 2});
    faces.emplace_back(master_vertices, std::vector<size_t>{0, 2, 3});

    IIIV::Solid cube(master_vertices, faces);
    EXPECT_EQ(cube.getFaces().size(), 2);
}