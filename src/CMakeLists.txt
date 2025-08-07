pybind11_add_module(iiiv bindings.cpp)

target_link_libraries(iiiv PRIVATE layerlib)
