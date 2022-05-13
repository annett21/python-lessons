first_line = list(input("First string: "))
second_line = list(input("Second string: "))


for shift in range(1, len(second_line) + 1):
    second_line.insert(0, second_line.pop())
    if second_line == first_line:
        print(f"You can get the first string out of the second with shift {shift}")
        break
else:
    print("You can't get the first string out of the second using shift")
