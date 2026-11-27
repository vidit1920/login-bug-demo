from flask import Flask, request, render_template_string

app = Flask(__name__)

USER = {"username": "admin", "password": "secret123"}

PAGE = """
<!DOCTYPE html>
<html>
<head><title>Login</title></head>
<body style="font-family: sans-serif; text-align: center; margin-top: 80px;">
  <h2>Login</h2>
  <form method="post">
    <input name="username" placeholder="Username" required><br><br>
    <input name="password" type="password" placeholder="Password" required><br><br>
    <button type="submit">Sign in</button>
  </form>
  <p style="color: {{ color }};">{{ message }}</p>
</body>
</html>
"""


def check_login(username, password):
    return username == USER["username"] or password == USER["password"]


@app.route("/", methods=["GET", "POST"])
def login():
    message, color = "", "black"
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        if check_login(username, password):
            message, color = f"Welcome, {username}!", "green"
        else:
            message, color = "Invalid username or password.", "red"
    return render_template_string(PAGE, message=message, color=color)


if __name__ == "__main__":
    app.run(debug=True)
