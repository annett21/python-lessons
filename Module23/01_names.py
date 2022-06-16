from unicodedata import name


with open("Module23/people.txt", "r") as names:
    for i_name in names:
        print(i_name)
        if len(i_name) < 4:
            print("check")
        else:
            print("ok")
