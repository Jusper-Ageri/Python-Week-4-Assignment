def read_and_write_file():
    # Ask user for filename
    input_file = input("Enter the filename to read: ")

    try:
        # Try opening the file
        with open(input_file, "r") as f:
            content = f.read()

        # Modifying the content (example: make everything uppercase)
        modified_content = content.upper()

        # Creating a new filename
        output_file = "modified_" + input_file

        # Writing modified content to the new file
        with open(output_file, "w") as f:
            f.write(modified_content)

        print(f"✅ Modified file saved as: {output_file}")

        # Exception handling
    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except PermissionError:
        print("❌ Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")


# Running the function
read_and_write_file()
