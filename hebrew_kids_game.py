# Key for Hebrew letters to special characters
hebrew_to_symbol = {
    'א': '@', 'ב': '$', 'ג': '%', 'ד': '^', 'ה': '&', 'ו': '*', 'ז': '~', 'ח': '<',
    'ט': '>', 'י': '{', 'כ': '}', 'ך': 'µ', 'ל': '[', 'מ': ']', 'ם': '≠', 'נ': ';',
    'ן': '≡', 'ס': '§', 'ע': '¤', 'פ': '©', 'ף': '≈', 'צ': '¶', 'ץ': '∑', 'ק': '°',
    'ר': '∞', 'ש': '=', 'ת': '+'
}

# Reverse key for decryption
symbol_to_hebrew = {v: k for k, v in hebrew_to_symbol.items()}


# Function to encrypt a message
def encrypt(hebrew_message):
    encrypted_message = ""
    for char in hebrew_message:
        if char in hebrew_to_symbol:
            encrypted_message += hebrew_to_symbol[char]  # Replace with the symbol if Hebrew letter
        else:
            encrypted_message += char  # Leave other characters (including numbers, punctuation) as is
    return encrypted_message


# Function to decrypt a message
def decrypt(encrypted_message):
    decrypted_message = ""
    for char in encrypted_message:
        if char in symbol_to_hebrew:
            decrypted_message += symbol_to_hebrew[char]  # Replace with the Hebrew letter if symbol
        else:
            decrypted_message += char  # Leave other characters as is
    return decrypted_message


# Main function to interact with the user
def main():
    message = input("Enter a Hebrew phrase: ")

    # Encrypt the message
    encrypted_message = encrypt(message)

    # Decrypt the message
    decrypted_message = decrypt(encrypted_message)

    print(f"Encrypted message: {encrypted_message}")
    print(f"Decrypted message: {decrypted_message}")


if __name__ == "__main__":
    main()
