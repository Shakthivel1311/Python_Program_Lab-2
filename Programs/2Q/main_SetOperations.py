import module_SetFunction as sf

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

sf.add_element(set1, 6)
print(f"Set1 after adding an element: {set1}")

sf.remove_element(set1, 6)
print(f"Set1 after removing an element: {set1}")

union, intersection = sf.union_intersection(set1, set2)
print(f"Union of Set1 and Set2: {union}")
print(f"Intersection of Set1 and Set2: {intersection}")

difference = sf.difference(set1, set2)
print(f"Difference of Set1 and Set2: {difference}")

is_subset = sf.is_subset(set1, set2)
print(f"Is Set1 a subset of Set2? {is_subset}")

length = sf.set_length(set1)
print(f"Length of Set1: {length}")

sym_diff = sf.symmetric_difference(set1, set2)
print(f"Symmetric difference of Set1 and Set2: {sym_diff}")

power_set = sf.power_set(set1)
print(f"Power set of Set1: {power_set}")

unique_subsets = sf.unique_subsets(set1)
print(f"Unique subsets of Set1: {unique_subsets}")
