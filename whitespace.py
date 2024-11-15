def ask_for_file():
    # Prompt user for the file containing the whitespace script
    file_path = input("Please provide the file path of the Whitespace script: ")
    return file_path

def read_whitespace_script(file_path):
    # Open and read the Whitespace code from the given file
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("File not found. Please check the path.")
        return None

def parse_whitespace_code(whitespace_code):
    # Initialize the stack and program counter (pc)
    stack = []
    pc = 0
    output = []

    # Go through each instruction in the whitespace code
    while pc < len(whitespace_code):
        char = whitespace_code[pc]

        if char == ' ':
            # Handling stack operations (example: push value)
            # If we have a series of spaces, it's a push operation
            pc += 1
            value = 0
            while pc < len(whitespace_code) and whitespace_code[pc] in ' \t':
                value = (value << 1) | (1 if whitespace_code[pc] == '\t' else 0)
                pc += 1
            stack.append(value)
            output.append(f"Pushed {value} to stack")
            
        elif char == '\t':
            # Handling other commands like arithmetic or I/O
            # (You can add other operations here for the tab-based instructions)
            pass  # You can expand this to handle more commands

        elif char == '\n':
            # Handle newlines to separate commands and end instructions
            pc += 1
            output.append("Instruction processed")

        # Moving program counter (pc)
        pc += 1

    # Convert stack of ASCII values to characters and join them as a string
    output_string = ''.join(chr(i) for i in stack if i != 0)  # Ignore 0 in stack
    output.append(f"Output: {output_string}")
    return stack, output

def main():
    # Ask for the file and read it
    file_path = ask_for_file()
    whitespace_code = read_whitespace_script(file_path)

    if whitespace_code:
        # Translate the code and show the result
        stack, output = parse_whitespace_code(whitespace_code)
        print("\nTranslation and Execution Result:")
        print("\n".join(output))
        print("\nFinal Stack:", stack)

if __name__ == "__main__":
    main()
