import module_ListFunction as lf

list1 = [x for x in range(1, 11)]         
list2 = [x**2 for x in range(1, 11)]      
list3 = [x for x in range(10, 0, -1)]     
list4 = [x for x in range(5)]            
list5 = [x * 1.5 for x in range(10)]      

example_list = list1

print(f"The list of Values is:{example_list}")
print(f"The maximum value is: {lf.find_max(example_list)}")
print(f"The minimum value is: {lf.find_min(example_list)}")
print(f"The sum of all elements is: {lf.calculate_sum(example_list)}")
print(f"The average of the list is: {lf.compute_average(example_list)}")
print(f"The median of the list is: {lf.determine_median(example_list)}")


