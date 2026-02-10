import pandas

data = pandas.read_csv("D:/100_Days_Code/Day26/nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

user_input = input("Enter a word: ").upper()

phonetic_word = [phonetic_dict[word] for word in user_input]

print(phonetic_word)