def check_password(password):
    if len(password) > 8:
        if password.islower() == False:
            if len([int(i) for i in password if i.isdigit()]) >= 3:
                return True

while 1:
    password = input("Create a password: ")
    if not check_password(password):
        print("Weak password.\nTry again")
    else:
        print("Congrats! You've got a strong password!")
        break
