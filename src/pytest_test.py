# Eksempel på en pytest. 
# Bemærk at navn på test-filer skal ende på _test.py.
# Bemærk også at navn på test-funktioner skal starte med test_

import mathematics


def test_add():
    assert mathematics.add(3, 4) == 7
