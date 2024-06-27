import os

"""
This script implements the Caesar Cipher encryption and decryption. The user can choose to either encrypt a text or decrypt a text from a file.
The encrypted text can be saved in a file, and the decrypted text is displayed in the terminal.
"""

def caesar_cipher(text, key, mode='encrypt'):
    result = ""
    for char in text:
        if char.isalpha():
            shift = ord(char.upper()) - ord('A')
            if mode == 'decrypt':
                shift -= key
            else:
                shift += key
            if char.isupper():
                result += chr((shift % 26) + ord('A'))
            else:
                result += chr((shift % 26) + ord('a'))
        else:
            result += char
    return result


def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def save_to_file(cipher_text):
    file_name = input("Enter the name of the file to save: ")
    if not file_name.endswith('.txt'):
        file_name += '.txt'
    with open(file_name, "a") as file:
        file.write(cipher_text)
    print("Encrypted text saved as: ", file_name)


def another_action():
    choice = input("Do you want to perform another action? (y/n): ")
    if choice.lower() == 'y':
        main()
    elif choice.lower() == 'n':
        print("\nSee you soon!")
    else:
        print("Invalid choice. Please enter 'y' for yes or 'n' for no.")
        another_action()


def main():
    choice = input("Encrypt or Decrypt? (e/d): ").lower()
    if choice == 'e':
        text = input("Enter the text to encrypt: ")
        key = int(input("Enter the encryption key (1-25): "))
        cipher_text = caesar_cipher(text, key, 'encrypt')
        save_to_file(cipher_text)
        another_action()
    elif choice == 'd':
        file_path = input("Enter the path to the file to decrypt: ")
        key = int(input("Enter the decryption key (integer): "))
        cipher_text = read_file(file_path)
        deciphered_text = caesar_cipher(cipher_text, key, 'decrypt')
        print("Decrypted text: ", deciphered_text)
        another_action()
    else:
        print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")
        another_action()


if __name__ == "__main__":
    main()
