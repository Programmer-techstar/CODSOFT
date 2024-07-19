import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    
    return password
    # Define a string containing all possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password using random.choices (Python 3.6+)
    password = ''.join(random.choices(characters, k=length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    print("----------------------------------")
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

   
    password = generate_password(length)
    print("Generated password:", password)

if __name__ == "__main__":
    main()