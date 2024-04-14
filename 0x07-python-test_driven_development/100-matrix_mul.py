#!/use/bin/python3

def matrix_mul(m_a, m_b):
    """
    Performs matrix multiplication between two matrices
        represented as lists of lists.

    Args:
        m_a (List[List[int or float]]): First matrix.
        m_b (List[List[int or float]]): Second matrix.

    Returns:
        List[List[int or float]]: Result of matrix multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list, or if any element within the
                   list of lists is not an integer or a float.
        ValueError: If m_a or m_b is empty ([] or [[]]).
        TypeError: If m_a or m_b isn't a rectangle (rows have varying lengths).
        ValueError: If m_a and m_b cannot multiplied (incompatible dimensions).
    """
    # Validating m_a and m_b both are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Validating m_a and m_b both are not empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # validating the conents of m_a
    for i in m_a:
        if not isinstance(i, list):
            raise TypeError("m_a must be a list of lists")
        for j in i:
            if not isinstance(j, int, float):
                raise TypeError("m_a should contain only integers or floats")
        if len(i) != len(m_a[-1]):
            raise TypeError("each row of m_a must be of the same size")

    # validating the conents of m_b
    for i in m_b:
        if not isinstance(i, list):
            raise TypeError("m_b must be a list of lists")
        for j in i:
            if not isinstance(j, int, float):
                raise TypeError("m_b should contain only integers or floats")
        if len(i) != len(m_b[-1]):
            raise TypeError("each row of m_b must be of the same size")
