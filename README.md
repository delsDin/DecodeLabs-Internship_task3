# Random Password Generator

A simple Python tool that generates random, complex passwords using letters and numbers.

![Python](https://img.shields.io/badge/Python-3.x-blue)

## Description

This project is part of the Decodelabs internship (task 3). It demonstrates key Python skills including:

- **Importing Modules**: Using `random` and `string` modules
- **String Manipulation**: Working with character sets and string concatenation

## How It Works

1. The user is prompted to enter the desired password length
2. The program generates a random password using:
   - Uppercase letters (A-Z)
   - Lowercase letters (a-z)
   - Digits (0-9)
3. The generated password is displayed to the user

## Usage

```bash
python3 main.py
```

### Example

```
=== RANDOM PASSWORD GENERATOR ===

Enter password length (e.g., 8): 12

Your generated password: kR4mNp9xLq2T

Keep it safe!
```

## Requirements

- Python 3

## Skills Demonstrated

| Skill | Implementation |
|-------|----------------|
| `import random` | Using `random.choice()` for random selection |
| `import string` | Using `string.ascii_letters` and `string.digits` |
| String manipulation | Concatenation with `+`, `join()` method |
| Input validation | Checking for positive integers |
| List comprehension | Generating random characters in a loop |

## Project Structure

```
week3/
├── main.py    # Main program
└── README.md  # This file
```