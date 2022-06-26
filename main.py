#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt") as file:
    content = file.readlines()
    # print(content)

with open("Input/Letters/starting_letter.txt") as file:
    letter_format = file.read()

for name in content:
    file_name = name.strip("\n")
    drafted_letter = letter_format.replace("____", file_name)
    with open(f"Output/ReadyToSend/{file_name}.txt", "w") as file:
        file.write(drafted_letter)



