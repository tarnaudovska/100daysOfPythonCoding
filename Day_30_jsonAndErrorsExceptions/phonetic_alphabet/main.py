# return the function untill you get name with alphabetic inputs
import pandas

#load your path for the nato_phonetic_alphabet.csv file
data = pandas.read_csv("./Day_30_jsonAndErrorsExceptions/phonetic_alphabet/nato_phonetic_alphabet.csv")
#dictionary from csv file
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

#Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = input("Enter a word to give you an alphabetic input for: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]   
    except KeyError:
        print ("Sorry, only letters in alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()
