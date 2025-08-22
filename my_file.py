
# File name called PROGRAMMER.txt
file_name = "assigment.txt"

# Open the file in write mode ("w" creates the file if it doesn't exist)
with open(file_name, "w") as file:
    file.write("Hello, this is my first file created using Python!\n")
    file.write("You can add multiple lines of text like this.\n")

print(f"File '{file_name}' has been created successfully.")