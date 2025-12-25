# convert list to dictionary
my_list = ['a', 'b', 'c', 'd']
my_dict = {}
for index in range(len(my_list)):
    my_dict[index] = my_list[index]
print(my_dict)
