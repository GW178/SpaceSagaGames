from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_hacking', methods=['POST'])
def start_hacking():
    ship_name = request.form['ship_name']
    difficulty = int(request.form['difficulty'])
    complicity = request.form['complicity']

    encrypted_password, numbers, letters, specials = generate_password(difficulty)

    if complicity == 'Easy':
        prompt = f"To hack the ship {ship_name}, type in the correct password of only numbers."
        correct_password = ''.join([char for char in encrypted_password if char in string.digits])
    elif complicity == 'Advanced':
        prompt = f"To hack the ship {ship_name}, type in the correct password of numbers and letters."
        correct_password_numbers = ''.join([char for char in encrypted_password if char in string.digits])
        correct_password_letters = ''.join([char for char in encrypted_password if char in string.ascii_lowercase])
        correct_password = correct_password_numbers + correct_password_letters
    elif complicity == 'Hard':
        prompt = f"To hack the ship {ship_name}, type in the correct password of numbers, letters, and specials."
        correct_password_numbers = ''.join([char for char in encrypted_password if char in string.digits])
        correct_password_letters = ''.join([char for char in encrypted_password if char in string.ascii_lowercase])
        correct_password_specials = ''.join([char for char in encrypted_password if char in string.punctuation])
        correct_password = correct_password_numbers + correct_password_letters + correct_password_specials

    # debug: print correct password to console to check it manually
    print(f"Correct password for {ship_name}: {correct_password}")

    return jsonify({
        'prompt': prompt,
        'encrypted_password': encrypted_password,
        'correct_password': correct_password
    })

@app.route('/hack', methods=['POST'])
def hack():
    user_password = request.form['user_password']
    correct_password = request.form['correct_password']
    ship_name = request.form['ship_name']

    # debugging: print correct vs user's password to check via console
    print(f"User password: {user_password}")
    print(f"Correct password: {correct_password}")

    if user_password == correct_password:
        message = f"Hacking successful, {ship_name} is hacked!"
        color = 'green'
    else:
        message = f"Hacking to {ship_name} failed."
        color = 'red'

    return jsonify({
        'message': message,
        'color': color
    })

if __name__ == "__main__":
    app.run(debug=True)