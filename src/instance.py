import src.design as design


class Instance:
    """
    An instance represents a design that is embedded in another design.

    Attributes:
        self._x_offset (int): x offset with respect to origin (0,0) of the parent design
        self._y_offset (int): y offset with respect to origin (0,0) of the parent design
        self._design_ref (Design): Reference to the embedded design

    Methods:
        def __init__(self):
            Initializes x and y offsets and reference design

        def set_offsets(self, x_offset: int, y_offset: int) -> None:
            Sets the offset with respect to origin of the parent design.

        def set_design_ref(self, design_ref) -> None:
            Sets the the reference for the embedded design

        def get_offset(self) -> int:
            Returns offset with respect to parent design

        def get_design_ref(self) -> Design:
            Returns the reference design
    """

    def __init__(self, x_offset, y_offset, design_ref):
        """Initializes x and y offsets and reference design

        Args:
            x_offset (int): x offset with respect to origin (0,0) of the parent design
            y_offset (int): y offset with respect to origin (0,0) of the parent design
            design_ref (Design): design that the instance will refer to
        Raises:
            TypeError: Raised if input parameters are not of expected type.
        """
        self.set_offsets(x_offset, y_offset)
        self.set_design_ref(design_ref)

    def set_offsets(self, x_offset: int, y_offset: int) -> None:
        """Sets the offset with respect to the origin (0, 0) of the parent design

        Args:
            x_offset (int): x offset with respect to origin (0,0) of the parent design
            y_offset (int): y offset with respect to origin (0,0) of the parent design

        Raises:
            TypeError: Raised if input parameters are not integers
        """
        if not isinstance(x_offset, int) or not isinstance(y_offset, int):
            error_message = 'Input paremeters are no of type int'
            print(error_message)
            raise TypeError(error_message)

        self._x_offset = x_offset
        self._y_offset = y_offset

    def set_design_ref(self, design_ref) -> None:
        """Sets the design object that represents the embedded design

        Args:
         design_ref (Design): design object that the embedded design will refer to

        Raises:
         TypeError: Raised if input parameter is not of type Design
        """
        if not isinstance(design_ref, design.Design):
            error_message = f'Input parameter {design_ref} is not of type Design'
            print(error_message)
            raise TypeError(error_message)

        self._design_ref = design_ref

    def get_offsets(self) -> int:
        """Returns offset with respect to parent design

        Returns:
           (Tuple[int]): (x_offset, y_offset)
        """
        return (self._x_offset, self._y_offset)

    def get_design_ref(self):
        """Gets the reference design

        Returns:
           (Design): The referenced design
        """
        return self._design_ref
