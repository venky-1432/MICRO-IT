
import random
import string

def generate_password(length):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine character sets
    all_chars = lowercase + uppercase + digits + special_chars

    # Ensure password has at least one character from each set
    password = [random.choice(lowercase), random.choice(uppercase), random.choice(digits), random.choice(special_chars)]

    # Fill the rest of the password length with random characters
    for _ in range(length - 4):
        password.append(random.choice(all_chars))

    # Shuffle the list to avoid the first four characters always being from specific sets
    random.shuffle(password)

    # Join the list into a string
    password = ''.join(password)

    return password

def main():
    # Prompt user for password length
    while True:
        try:
            length = int(input("Enter the desired password length (min 4): "))
            if length < 4:
                print("Password length should be at least 4.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Generate and display password
    password = generate_password(length)
    print("Generated Password: ", password)

if __name__ == "__main__":
    main()
