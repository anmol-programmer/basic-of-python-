# Merge two lists and remove duplicates
# This script merges two lists and removes any duplicate elements.
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

merged = list1 + list2
unique_list = []
for item in merged:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)
