import random
import string

def generate_random_string(length):
    characters = string.ascii_uppercase + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def main():
    print("-------------")
    print("A8ton-Password-Generator")
    print("-------------")
    
    try:
        length = int(input("Enter the number of digits and letters: "))
        if length <= 0:
            raise ValueError("The number must be positive.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    random_string = generate_random_string(length)
    print(f"Randomly generated string: {random_string}")

if __name__ == "__main__":
    main()