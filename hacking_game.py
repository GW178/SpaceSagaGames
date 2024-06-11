import random
import string


def generate_password(difficulty):
    if difficulty == 1:
        nums, lets, specs = 3, 3, 4
    elif difficulty == 2:
        nums, lets, specs = 5, 5, 5
    elif difficulty == 3:
        nums, lets, specs = 7, 7, 6
    else:
        raise ValueError("Invalid difficulty level. Choose 1, 2, or 3.")

    numbers = random.choices(string.digits, k=nums)
    letters = random.choices(string.ascii_lowercase, k=lets)
    specials = random.choices(string.punctuation, k=specs)

    password = numbers + letters + specials
    random.shuffle(password)
    encrypted_password = ''.join(password)

    return encrypted_password, numbers, letters, specials


def hacking_game():
    ship_name = input("Enter ship's name: ")

    try:
        difficulty = int(input("Pick difficulty level (1/2/3): "))
        if difficulty not in [1, 2, 3]:
            raise ValueError
    except ValueError:
        print("Invalid difficulty level. Please choose 1, 2, or 3.")
        return

    complicity = input("Pick Complicity level (Easy, Advanced, Hard): ")
    if complicity not in ['Easy', 'Advanced', 'Hard']:
        print("Invalid complicity level. Please choose Easy, Advanced, or Hard.")
        return

    encrypted_password, numbers, letters, specials = generate_password(difficulty)

    if complicity == 'Easy':
        prompt = f"To hack the ship {ship_name}, type in the correct password of only numbers."
        correct_password = ''.join(numbers)
    elif complicity == 'Advanced':
        prompt = f"To hack the ship {ship_name}, type in the correct password of numbers and letters."
        correct_password = ''.join(numbers + letters)
    elif complicity == 'Hard':
        prompt = f"To hack the ship {ship_name}, type in the correct password of numbers, letters, and specials."
        correct_password = ''.join(numbers + letters + specials)

    print(prompt)
    print(f"Encrypted password: {encrypted_password}")

    user_password = input()

    correct_numbers = ''.join([char for char in encrypted_password if char in string.digits])
    correct_letters = ''.join([char for char in encrypted_password if char in string.ascii_letters])
    correct_specials = ''.join([char for char in encrypted_password if char in string.punctuation])

    if complicity == 'Easy':
        correct_password = correct_numbers
    elif complicity == 'Advanced':
        correct_password = correct_numbers + correct_letters
    elif complicity == 'Hard':
        correct_password = correct_numbers + correct_letters + correct_specials

    if user_password == correct_password:
        print(f"Hacking successful, {ship_name} is hacked!")
    else:
        print(f"Hacking to {ship_name} failed.")


if __name__ == "__main__":
    hacking_game()