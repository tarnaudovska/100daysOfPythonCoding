# Caesar Cipher Program (encrypt and decode your text)

## Description
This Python script implements the **Caesar Cipher**, a simple encryption technique used to encode and decode messages by shifting letters of the alphabet by a specified amount. 

The program allows users to:
- Encode a message.
- Decode a message.
- Retain special characters, numbers, and spaces without altering them.
- Restart the program multiple times if desired.

---

## Features
- **Flexible Shifting**: Handles shifts greater than 26 by wrapping around the alphabet.
- **Case Insensitivity**: Converts all text to lowercase for simplicity.
- **Character Preservation**: Leaves numbers, symbols, and spaces unaltered.
- **Interactive CLI**: Asks the user to encode, decode, and restart the program as needed.

---

## Usage

### 1. Inputs Required:
- **Direction**: Specify whether to `encode` or `decode`.
- **Message**: Enter the message you want to encrypt or decrypt.
- **Shift**: Specify the number of shifts for the cipher.

### 2. Example Run:
```plaintext
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello world!
Type the shift number:
5
Here's the encoded result: mjqqt btwqi!
Do you want to restart the cipher program? Yes or No => no
