
def modify_file(input_file, output_file):
    """Reads a file, modifies its content, and writes to a new file."""
    if not os.path.exists(input_file):
        print(f"❌ '{input_file}' not found! Creating a new one...")
        with open(input_file, "w") as file:
            file.write("This is a sample text file.\nEdit and run again.")
        return
    
    try:
        with open(input_file, "r") as infile:
            content = infile.read()

        # Modify content (convert text to uppercase)
        modified_content = content.upper()

        with open(output_file, "w") as outfile:
            outfile.write(modified_content)

        print(f"✅ Modified content written to '{output_file}'")
    
    except Exception as e:
        print(f"❌ Unexpected error: {e}")