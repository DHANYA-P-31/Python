# TODO: Create a letter using starting_letter.txt
with open("./Input/Letters/starting_letter.txt") as file:
    message = file.read()
    with open("./Input/Names/invited_names.txt") as f:
        for word in f.readlines():
            with open(f"Output/ReadyToSend/{word.strip()}.txt","w")as wd:
                wd.write(message.replace("[name]",word.strip()))
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp