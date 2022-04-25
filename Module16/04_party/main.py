guests = ["Peter", "Ivan", "Alex", "Lisa", "Kate"]

while True:
    print(f"There are {len(guests)} guests at the party:", guests)

    user_input = input("Has a guest come or left? (come/left/time to sleep) ")

    if user_input not in ("come", "left", "time to sleep"):
        continue

    if user_input == "time to sleep":
        print("The party is over.")
        break

    guest_name = input("Name of guest: ")

    if user_input == "left":
        if guest_name not in guests:
            print(f"There is no {guest_name} here.")
            continue

        guests.remove(guest_name)
        print(f"Bye, {guest_name}")

    elif user_input == "come":
        if len(guests) >= 6:
            print(f"Sorry, {guest_name}, but there is no place.")
            continue

        guests.append(guest_name)
        print(f"Hi, {guest_name}")
