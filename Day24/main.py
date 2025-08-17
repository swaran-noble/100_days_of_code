PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as invited:
    invited_names = []
    contents = invited.readlines()
    for content in contents:
        invited_names.append(content.strip('\n'))

with open("./Input/Letters/starting_letter.txt") as template:
    contents = template.read()
    for name in invited_names:
        with open(f"Output/ReadyToSend/Letter_to_{name}.txt","w") as letter:
            replaced_content = contents.replace(PLACEHOLDER,f"{name}")
            letter.write(replaced_content)

    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp