def str_list(input_list):
    """
    Convert all the elements in a list to str
    :param input_list:
    :type input_list: list[any
    :return: list including str elements
    :rtype list[str]
    """
    return ['{}'.format(e) for e in input_list]

if __name__ == "__main__":
    input_list = ['a', 0]
    print(str_list(input_list))