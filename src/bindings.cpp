#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "Vertex.h"
#include "Face.h"
#include "Plane.h"
#include "Solid.h"

namespace py = pybind11;

PYBIND11_MODULE(iiiv, m) {
    py::class_<IIIV::Vertex>(m, "Vertex")
        .def(py::init<double, double, double>())
        .def("getX", &IIIV::Vertex::getX)
        .def("getY", &IIIV::Vertex::getY)
        .def("getZ", &IIIV::Vertex::getZ)
        .def("setX", &IIIV::Vertex::setX)
        .def("setY", &IIIV::Vertex::setY)
        .def("setZ", &IIIV::Vertex::setZ)
        .def("project", py::overload_cast<const IIIV::Plane&>(&IIIV::Vertex::project, py::const_), py::arg("plane"))
        .def("project", py::overload_cast<>(&IIIV::Vertex::project, py::const_));

    py::class_<IIIV::Plane>(m, "Plane")
        .def(py::init<double, double, double, double>())
        .def("getA", &IIIV::Plane::getA)
        .def("getB", &IIIV::Plane::getB)
        .def("getC", &IIIV::Plane::getC)
        .def("getD", &IIIV::Plane::getD);

    py::class_<IIIV::Face>(m, "Face")
        .def(py::init([](const std::vector<IIIV::Vertex>& all_vertices_py, const std::vector<size_t>& vertex_indices_py) {
            // Create a shared_ptr to a new vector, copying the Python list content
            auto all_vertices_cpp = std::make_shared<std::vector<IIIV::Vertex>>(all_vertices_py);
            return IIIV::Face(all_vertices_cpp, vertex_indices_py);
        }), py::arg("all_vertices"), py::arg("vertex_indices"))
        .def("getVertices", &IIIV::Face::getVertices)
        .def("getNormal", &IIIV::Face::getNormal, py::return_value_policy::reference)
        .def("getPlaneEquation", &IIIV::Face::getPlaneEquation)
        .def("invert", &IIIV::Face::invert)
        .def("project", py::overload_cast<const IIIV::Plane&>(&IIIV::Face::project, py::const_), py::arg("plane"))
        .def("project", py::overload_cast<>(&IIIV::Face::project, py::const_));

    py::class_<IIIV::Solid>(m, "Solid")
        .def(py::init([](const std::vector<IIIV::Vertex>& all_vertices_py, const std::vector<IIIV::Face>& faces_py) {
            auto all_vertices_cpp = std::make_shared<std::vector<IIIV::Vertex>>(all_vertices_py);
            return IIIV::Solid(all_vertices_cpp, faces_py);
        }), py::arg("all_vertices"), py::arg("faces"))
        .def("getFaces", &IIIV::Solid::getFaces, py::return_value_policy::reference)
        .def("project", py::overload_cast<const IIIV::Plane&>(&IIIV::Solid::project, py::const_), py::arg("plane"))
        .def("project", py::overload_cast<>(&IIIV::Solid::project, py::const_));
}