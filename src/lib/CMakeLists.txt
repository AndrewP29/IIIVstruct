add_library(layerlib Vertex.cpp Face.cpp Solid.cpp Plane.cpp)

target_include_directories(layerlib PUBLIC ../../include)

# Link Clipper2 and define macro when available via FetchContent
if(TARGET Clipper2::Clipper2)
  target_link_libraries(layerlib PUBLIC Clipper2::Clipper2)
  target_compile_definitions(layerlib PUBLIC IIIV_HAVE_CLIPPER2=1)
endif()
