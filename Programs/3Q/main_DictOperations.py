import module_DictFunction as mf

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 4, 'd': 5}
dict3 = {'a': 1, 'd': 5, 'e': 6}

merged_dict = mf.merging_Dict(dict1, dict2, dict3)
print(f"Merged Dictionary: {merged_dict}")

common_keys = mf.common_keys(dict1, dict2, dict3)
print(f"Common Keys: {common_keys}")

inverted_dict = mf.invert_dict(dict1)
print(f"Inverted Dictionary: {inverted_dict}")

common_kv_pairs = mf.common_key_value_pairs(dict1, dict2, dict3)
print(f"Common Key-Value Pairs: {common_kv_pairs}")
