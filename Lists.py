numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

second_name = names[1]
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append('hello')
strings.append('world')


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

new_list = [1, 2, 3, 6]
new_list[3:7] = [4, 5, 6]
new_list.append(7)
new_list.append(9)
new_list[7:8] = []
new_list.reverse()
new_list[7:] =  [0, 0, 0]
print(new_list)
print(f'The lenght of the new_list is {len(new_list)} elements')
print(f'And digit 0 occurs {new_list.count(0)} times in the "new_list" list')
