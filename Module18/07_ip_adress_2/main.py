ip = input("Enter IP: ")

updated_ip = ip.split(".")

if len(updated_ip) != 4:
    print("Adress is 4 numbers, devided by a point.")
else:
    for digit in updated_ip:
        if not digit.isdigit():
            print(f"{digit} - not an integer.")
            break
        if int(digit) < 0 or int(digit) > 255:
            print(f"{digit} is greater then 255.")
            break
    else:
        print("IP is correct.")
