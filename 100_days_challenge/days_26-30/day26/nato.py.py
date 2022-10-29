
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_keywords = {row.letter: row.code for (index, row) in data.iterrows()}

my_word = input("What is the word: ").upper()
nato_list = [nato_keywords[letter] for letter in my_word]
print(nato_list)