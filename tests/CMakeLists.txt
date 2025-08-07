add_executable(test_vector test_vector.cpp)
target_link_libraries(test_vector layerlib)

add_test(NAME test_vector COMMAND test_vector)

add_executable(test_face test_face.cpp)
target_link_libraries(test_face layerlib)

add_test(NAME test_face COMMAND test_face)
