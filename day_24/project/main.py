import os

#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Read the names from invited_names.txt
with open('day_24/project/Input/Names/invited_names.txt') as names_file:
    names = names_file.readlines()

# Read the starting letter template
with open('day_24/project/Input/Letters/starting_letter.txt') as letter_file:
    letter_template = letter_file.read()

# Create the output directory if it doesn't exist
output_dir = 'day_24/project/Output/ReadyToSend'
os.makedirs(output_dir, exist_ok=True)

# Generate and save letters for each name
for name in names:
    name = name.strip()  # Remove any extra whitespace
    personalized_letter = letter_template.replace('[name]', name)
    
    with open(f'{output_dir}/{name}.txt', 'w') as letter:
        letter.write(personalized_letter)