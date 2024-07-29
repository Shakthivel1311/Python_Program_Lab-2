def merging_Dict(*args):
    result = {}
    for dictionary in args:
        result.update(dictionary)
    return result

def common_keys(*args):
    if not args:
        return set()
    common = set(args[0].keys())
    for dictionary in args[1:]:
        common &= set(dictionary.keys())
    return common

def invert_dict(d):
    inverted = {}
    for key, value in d.items():
        if value in inverted:
            if isinstance(inverted[value], list):
                inverted[value].append(key)
            else:
                inverted[value] = [inverted[value], key]
        else:
            inverted[value] = key
    return inverted

def common_key_value_pairs(*args):
    if not args:
        return {}
    common = args[0].items()
    for dictionary in args[1:]:
        common &= dictionary.items()
    return dict(common)
