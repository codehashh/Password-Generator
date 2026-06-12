from flask import Flask, render_template, request
import secrets
import string

app = Flask(__name__)

def generate_password(length, upper, lower, numbers, symbols):
    chars = ""

    if upper:
        chars += string.ascii_uppercase

    if lower:
        chars += string.ascii_lowercase

    if numbers:
        chars += string.digits

    if symbols:
        chars += string.punctuation

    if not chars:
        return "Select at least one option!"

    password = ''.join(secrets.choice(chars) for _ in range(length))
    return password

@app.route("/", methods=["GET", "POST"])
def home():
    password = ""
    strength = ""

    if request.method == "POST":
        length = int(request.form.get("length", 12))

        upper = request.form.get("uppercase")
        lower = request.form.get("lowercase")
        numbers = request.form.get("numbers")
        symbols = request.form.get("symbols")

        password = generate_password(
            length,
            upper,
            lower,
            numbers,
            symbols
        )

        score = 0

        if len(password) >= 8:
            score += 1
        if len(password) >= 12:
            score += 1
        if any(c.isupper() for c in password):
            score += 1
        if any(c.isdigit() for c in password):
            score += 1
        if any(not c.isalnum() for c in password):
            score += 1

        if score <= 2:
            strength = "Weak"
        elif score == 3:
            strength = "Medium"
        elif score == 4:
            strength = "Strong"
        else:
            strength = "Very Strong"

    return render_template(
        "index.html",
        password=password,
        strength=strength
    )

if __name__ == "__main__":
    app.run(debug=True)