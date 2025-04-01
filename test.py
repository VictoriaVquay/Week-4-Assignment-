def modify_content(content):
    """Modify the content as needed. Here, we convert it to uppercase."""
    return content.upper()

try:
    filename = input("Enter the filename to read: ")
    with open(filename, "r") as file:
        content = file.read()
    
    modified_content = modify_content(content)
    
    new_filename = "modified_" + filename
    with open(new_filename, "w") as file:
        file.write(modified_content)
    
    print(f"Modified content written to {new_filename}")
except FileNotFoundError:
    print("Error: File not found. Please check the filename and try again.")
except IOError:
    print("Error: Unable to read the file. Please check permissions.")
