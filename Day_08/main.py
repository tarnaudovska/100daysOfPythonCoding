def calculate_love_score(name1, name2):
    true_counter=0
    love_counter=0
    names = name1 + name2
    true = "true"
    love = "love"
    for letter in names:
        if letter.lower() in true:
            true_counter+=1
    for letter in names:
        if letter.lower() in love:
            love_counter+=1
    return str(true_counter) + str(love_counter)

name1 = input("Input the first name for the love calculator\n")
name2 = input("Input the second name for the love calculator\n")

print(f"The love score for {name1} and {name2} is {calculate_love_score(name1, name2)}")