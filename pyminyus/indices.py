def indices(x_list, v_list, include=True):
    """ Get indices of elements in x_list which are (not) included in the v_list
    Args:
        x_list: the target list
        v_list: (list of) values
        include: x_list includes each value or not
    """
    if not isinstance(v_list, list):
        v_list = [v_list]
    if include:
        return [index for index, x in enumerate(x_list) if x in v_list]
    if not include:
        return [index for index, x in enumerate(x_list) if x not in v_list]


if __name__ == "__main__":
    print(indices([0, 1, 0, 1, 0], 0, False))  # returns [1, 3]
