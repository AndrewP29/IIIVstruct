#include "Solid.h"

namespace IIIV {

Solid::Solid(std::shared_ptr<std::vector<Vertex>> all_vertices, const std::vector<Face>& faces)
    : vertices_ptr_(all_vertices), faces_(faces) {}

const std::vector<Face>& Solid::getFaces() const {
    return faces_;
}

} // namespace IIIV
