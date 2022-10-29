#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

PLACEHOLDER = "[name]"

with open("./input/names/invited_names.txt") as names_list: 
    # To get rid of unwanted /n
    names = [name.strip() for name in names_list.readlines()]
   

with open("./input/letters/starting_letter.txt") as template_file: 
    for name in names:
       with open(f"./output/readytosend/letter_for_{name}.txt", mode="w") as final: 
           final.write(template_file.read().replace(PLACEHOLDER, name))
           




    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp