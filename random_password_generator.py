import random
import string

def random_password_generator(length, use_letters=True, use_symbols=True, use_numbers=True):
    characters = ""

    if use_letters:
        characters += string.ascii_letters
    if use_symbols:
        characters += string.punctuation
    if use_numbers:
        characters += string.digits

    if not characters:
        print("Error: Please select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_valid_length():
    while True:
        try:
            length = int(input("Enter the password length: "))
            return length
        except ValueError:
            print("Error: Please enter a valid integer for password length.")

def get_yes_no_input(message):
    while True:
        user_input = input(message).lower()
        match user_input:
            case 'y':
                return True
            case 'n':
                return False
            case _:
                print('Please enter either "y" or "n".')


def main():
    print("Welcome to the Command-line Password Generator!")

    length = get_valid_length()
    use_letters = get_yes_no_input("Include letters? (y/n): ")
    use_symbols = get_yes_no_input("Include symbols? (y/n): ")
    use_numbers = get_yes_no_input("Include numbers? (y/n): ")

    password = random_password_generator(length, use_letters, use_symbols, use_numbers)

    if password:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
