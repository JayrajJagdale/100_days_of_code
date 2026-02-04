with open("D:/100_Days_Code/Day24/Input/Names/invited_names.txt") as names_file:
        names =  names_file.readlines()
        

with open("D:/100_Days_Code/Day24/Input/Letters/starting_letter.txt") as letter_file:
        letter_contents = letter_file.read()
        for name in names:
            strip_name = name.strip("\n")
            new_letter = letter_contents.replace("[name]", strip_name)

            with open(f"D:/100_Days_Code/Day24/Output/ReadyToSend/letter_for_{strip_name}.txt", mode="w") as updated_file:
              updated_file.write(new_letter)