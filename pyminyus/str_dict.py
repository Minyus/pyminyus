def str_dict(input_dict):
    """
    Convert all the values in a dictionary to str
    :param input_dict:
    :type input_dict: dict{any: any]
    :return: dictionary including str values
    :rtype dict[any: str]
    """
    return {key: "{}".format(value) for key, value in input_dict.items()}


if __name__ == "__main__":
    input_dict = {"key0": 123, "key1": "text"}
    print(str_dict(input_dict))
