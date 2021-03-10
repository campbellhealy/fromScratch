old_list = [10,2,3,14,50,6,7,8,9]

new_list = [item for item in old_list[::2] if item % 2 == 0]

print(new_list)

# old_list = [5, 12, 3, 21, 8, 7, 19, 102]
# new_list = old_list[::2]

# print("new_list: " + str(new_list))
