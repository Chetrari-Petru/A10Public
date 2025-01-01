class ValidationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class SizeMismatchError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)



def validate_tuple(list_of_types: list, _tuple: tuple):
    """
    Validates a tuple of 1x#listOfTypes size
    :param list_of_types: The Types of each tuple position
    :param _tuple: The tuple to be validated
    :raises Validation Error
    """
    try:
        for i in range(len(list_of_types)):
            if type(_tuple[i]) != list_of_types[i]:
                raise ValidationError("parameter of index {0} is not of type {1}".format(i, list_of_types[i]))
    except IndexError:
        raise SizeMismatchError("Tuple is not of the same size as list_of_types")