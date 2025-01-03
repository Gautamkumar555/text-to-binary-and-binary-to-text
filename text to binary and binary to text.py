def text_to_binary(text):
    return ' '.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary):
    try:
        return ''.join(chr(int(b, 2)) for b in binary.split())
    except ValueError:
        return "Invalid binary input!"

while True:
    print("\nChoose an option:")
    print("1. Code (Text to Binary)")
    print("2. Decode (Binary to Text)")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        text = input("Enter the sentence to encode: ")
        print(f"Binary Code: {text_to_binary(text)}")
    elif choice == "2":
        binary = input("Enter the binary to decode: ")
        print(f"Decoded Text: {binary_to_text(binary)}")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
