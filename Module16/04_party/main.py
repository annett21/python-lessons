guests = ["Peter", "Ivan", "Alex", "Lisa", "Kate"]

while True:
    print(f"There are {len(guests)} friends at the party right now:", guests)
    answer = input("Have the guest come or left? ")
    if answer == "sleep time":
        print("The party is over, everybody is sleeping.")
        break
    name = input("Guest name: ")
    if answer == "come":
        if len(guests) >= 6:
            print(f"Sorry, {name}, we're full.")
        elif len(guests) < 6:
            guests.append(name)
            print(f"Hello, {name}!")
    elif answer == "left":
        print(f"Bye, {name}!")
        guests.remove(name)
