#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "Vector.h"
#include "Face.h"
#include "Plane.h"

namespace py = pybind11;

PYBIND11_MODULE(iiiv, m) {
    py::class_<IIIV::Vector>(m, "Vector")
        .def(py::init<double, double, double>())
        .def("getX", &IIIV::Vector::getX)
        .def("getY", &IIIV::Vector::getY)
        .def("getZ", &IIIV::Vector::getZ)
        .def("setX", &IIIV::Vector::setX)
        .def("setY", &IIIV::Vector::setY)
        .def("setZ", &IIIV::Vector::setZ);

    py::class_<IIIV::Plane>(m, "Plane")
        .def_readwrite("normal", &IIIV::Plane::normal)
        .def_readwrite("d", &IIIV::Plane::d);

    py::class_<IIIV::Face>(m, "Face")
        .def(py::init<const std::vector<IIIV::Vector>&>())
        .def("getVertices", &IIIV::Face::getVertices, py::return_value_policy::reference)
        .def("getPlaneEquation", &IIIV::Face::getPlaneEquation);
}
