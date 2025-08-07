# Enable CTest
enable_testing()

# Create the test executable
add_executable(
  run_tests
  test_vertex.cpp
  test_face.cpp
)

# Link against our library and Google Test
target_link_libraries(
  run_tests
  GTest::gtest_main
  layerlib
)

# Add the test to CTest
include(GoogleTest)
gtest_discover_tests(run_tests)