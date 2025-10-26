def caesar_cipher(text, shift, mode="encrypt"):
    result = ""

    if mode == "decrypt":
        shift = -shift  

    for char in text:
        if char.isalpha(): 
            shift_start = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - shift_start + shift) % 26 + shift_start)
            result += new_char
        else:
            result += char  

    return result

# User input
message = input("Enter the message: ")
shift_value = int(input("Enter the shift value: "))
operation = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()

# Process the input
output = caesar_cipher(message, shift_value, operation)
print("Result:", output)