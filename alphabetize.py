
# Initialize the files to be used for this tool
input_file = "List.txt"
output_file = "NewList.txt"

# open the input file and have a variable hold the contents
try:
        with open(input_file) as f:
            content = f.readlines()
            
# If there is no file found with this name, output an error            
except FileNotFoundError:
    print(f"Error: the file '{input_file}' does not exist.")
    exit(1)
    
# Split the text into a list of lines via removing any leading/trailing whitespace
content = [line.strip() for line in content]

# Alphabetize the list via the sort function
content.sort()

# Write the new alphabetized list to the new output file
try:
    with open(output_file, "w") as f:
        for line in content:
            f.write(line + "\n")
            
# If no file with this name has been found
except IOError:
    print(f"Error: could not write to file '{output_file}'.")
    exit(1)
    
print("Successfully alphabetized List.txt")
