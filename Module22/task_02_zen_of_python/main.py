def reverse_file_text(file_path):
    with open(file_path, "r") as text:
        for i_text in reversed(text.readlines()):
            print(i_text, end="")


reverse_file_text("Module22/02_zen_of_python/zen.txt")
