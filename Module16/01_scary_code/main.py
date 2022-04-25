# a = [1, 5, 3]
# b = [1, 5, 1, 5]
# c = [1, 3, 1, 5, 3, 3]
# for i in b:
#     a.append(i)
# t = 0
# for i in a:
#     if i == 5:
#         t += 1
# print(t)
# d = []
# for i in a:
#     if i != 5:
#         d.append(i)
# for i in c:
#     d.append(i)
# t = 0
# for i in d:
#     if i == 3:
#         t += 1
# print(t)
# print(d)

main_list = [1, 5, 3]
first_side_list = [1, 5, 1, 5]
second_side_list = [1, 3, 1, 5, 3, 3]

main_list.extend(first_side_list)
print("Count of 5:", main_list.count(5))
for _ in range(main_list.count(5)):
    main_list.remove(5)

main_list.extend(second_side_list)
print("Count of 3:", main_list.count(3))

print("The result list:", main_list)
