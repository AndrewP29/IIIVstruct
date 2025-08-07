#include <pybind11/pybind11.h>
#include "Vector.h"

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
}
