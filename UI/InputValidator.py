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
    :return: The converted tuple
    :raises Validation Error
    """

    tuple_list = []
    try:
        for i in range(len(list_of_types)):
            try:
                tuple_list.insert(i, list_of_types[i](_tuple[i]))
            except ValueError:
                raise ValidationError("parameter of index {0} is not of _type {1}".format(i, list_of_types[i]))
            
    except IndexError:
        raise SizeMismatchError("Tuple is not of the same size as list_of_types")

    return tuple(tuple_list)

def validate_v2(_type, vector2):
    """
    Validates a Vector 2
    :param _type: Type of data stored in the vector
    :param vector2: The vector to be validated
    :return: The converted vector
    :raises Validation Error
    """

    try:
        vector2.x = _type(vector2.x)
    except ValueError:
        raise  ValidationError("parameter of index {0} is not of _type {1}".format(vector2.x, _type))

    try:
        vector2.y = _type(vector2.y)
    except ValueError:
        raise ValidationError("parameter of index {0} is not of _type {1}".format(vector2.y, _type))

    return vector2