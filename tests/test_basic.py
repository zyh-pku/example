import example_0

def test_compare():
    a = example_0.Vector(1,2)
    b = example_0.Vector(1,2)

    assert a.x == b.x
    assert a.y == b.y
    assert a == b
