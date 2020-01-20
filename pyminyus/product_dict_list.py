from itertools import product


def product_dict_list(d):
    """
    Generate all the combinations of dictionary values.
    :param d:
    :type d: dict[str, list[any]]
    :return list of combinations of values
    :rtype list[dict[str, any]]
    """
    return list(dict(zip(d.keys(), values)) for values in product(*d.values()))


if __name__ == "__main__":
    params_dict = {
        "filters": [32, 64],
        "kernel_size": [3, 4],
        "activation": ["relu", "linear"],
    }
    print("input:", params_dict, "\n")
    params_list = product_dict_list(params_dict)
    print("output:")
    for p in params_list:
        print(p)
