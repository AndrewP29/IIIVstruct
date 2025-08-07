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

TEST_F(SolidTest, ClosedCube) {
    std::vector<IIIV::Face> faces;

    // Front face (0,1,2,3)
    faces.emplace_back(master_vertices, std::vector<size_t>{0, 1, 2});
    faces.emplace_back(master_vertices, std::vector<size_t>{0, 2, 3});

    // Back face (4,7,6,5) - inverted normal
    faces.emplace_back(master_vertices, std::vector<size_t>{4, 7, 6});
    faces.emplace_back(master_vertices, std::vector<size_t>{4, 6, 5});

    // Right face (1,5,6,2)
    faces.emplace_back(master_vertices, std::vector<size_t>{1, 5, 6});
    faces.emplace_back(master_vertices, std::vector<size_t>{1, 6, 2});

    // Left face (0,3,7,4)
    faces.emplace_back(master_vertices, std::vector<size_t>{0, 3, 7});
    faces.emplace_back(master_vertices, std::vector<size_t>{0, 7, 4});

    // Top face (3,2,6,7)
    faces.emplace_back(master_vertices, std::vector<size_t>{3, 2, 6});
    faces.emplace_back(master_vertices, std::vector<size_t>{3, 6, 7});

    // Bottom face (0,4,5,1) - inverted normal
    faces.emplace_back(master_vertices, std::vector<size_t>{0, 4, 5});
    faces.emplace_back(master_vertices, std::vector<size_t>{0, 5, 1});

    IIIV::Solid cube(master_vertices, faces);
    EXPECT_TRUE(cube.isClosed());
}

TEST_F(SolidTest, OpenCube) {
    std::vector<IIIV::Face> faces;

    // Front face only (0,1,2,3)
    faces.emplace_back(master_vertices, std::vector<size_t>{0, 1, 2});
    faces.emplace_back(master_vertices, std::vector<size_t>{0, 2, 3});

    IIIV::Solid open_solid(master_vertices, faces);
    EXPECT_FALSE(open_solid.isClosed());
}
