import pytest
from src.shape import Shape
from src.design import Design


def test_add_shape_type_error():
    """Design.add_shape() must raise TypeError if it is passed an object which is not a shape
    """
    test_design = Design()
    with pytest.raises(TypeError):
        test_design.add_shape("not a shape")


def test_get_shapes_1():
    """Design.get_shapes() must return an empty list if no shapes have been added to the design
    """
    test_design = Design()
    retrieved_shapes = test_design.get_shapes()
    assert retrieved_shapes == []


def test_add_get_shapes_1():
    """Design.get_shapes() can returns copies of shapes added by Design.add_shapes()
    """
    test_design = Design()
    shape_1 = Shape(0, 0, 1, 1)
    shape_2 = Shape(1, 1, 2, 2)
    test_design.add_shape(shape_1)
    test_design.add_shape(shape_2)
    retrieved_shapes = test_design.get_shapes()
    assert retrieved_shapes == [shape_1, shape_2]


def test_added_shape_copy():
    """Design.add_shapes() returns a copy of the shape it created an added to the design
    """
    test_design = Design()
    shape_1 = Shape(0, 1, 2, 3)
    shape_1_copy = test_design.add_shape(shape_1)
    assert shape_1 == shape_1_copy  # added copy has same offset and dimensions
    shape_1.set_offset(5, 5)
    assert shape_1 != shape_1_copy  # changing original shape does not affect copy


def test_get_shapes_descending_area_1():
    """Design.get_shapes_descending_area returns shapes sorted by area (descending order)
    """
    test_design = Design()
    shape_1 = Shape(0, 0, 1, 1)
    shape_2 = Shape(0, 0, 1, 1)
    shape_3 = Shape(0, 0, 5, 5)
    shape_4 = Shape(0, 0, 2, 2)
    test_design.add_shape(shape_1)
    test_design.add_shape(shape_2)
    test_design.add_shape(shape_3)
    test_design.add_shape(shape_4)
    sorted_shapes = test_design.get_shapes_descending_area()
    assert sorted_shapes == [shape_3, shape_4, shape_1, shape_2]
