file = open("D:/100_Days_Code/Day24/my_file.txt")
contents = file.read()
print(contents)
file.close()

with open("D:/100_Days_Code/Day24/my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("D:/100_Days_Code/Day24/my_file.txt", mode="w") as file:
    file.write("New Text.")

with open("D:/100_Days_Code/Day24/my_file.txt", mode="a") as file:
    file.write("\nNew Text Append.")

with open("new_file.txt", mode="w") as file:
    file.write("If file not exists then it create new file..")