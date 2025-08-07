#include "Vector.h"
#include <cassert>

void test_vector() {
    IIIV::Vector v(1.0, 2.0, 3.0);
    assert(v.getX() == 1.0);
    assert(v.getY() == 2.0);
    assert(v.getZ() == 3.0);

    v.setX(4.0);
    v.setY(5.0);
    v.setZ(6.0);
    assert(v.getX() == 4.0);
    assert(v.getY() == 5.0);
    assert(v.getZ() == 6.0);
}

int main() {
    test_vector();
    return 0;
}
