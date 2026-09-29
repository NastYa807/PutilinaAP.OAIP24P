from flask import Flask, render_template, request

app = Flask(__name__)

VALID_USERNAME = "administrator"
VALID_PASSWORD = "88888"


@app.route('/')
def login_page():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def handle_login():
    username = request.form['username']
    password = request.form['password']

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        return render_template(
            'login.html',
            message="Вход успешно выполнен",
            message_type="success",
            show_link=True
        )
    else:
        return render_template(
            'login.html',
            message="Неверный логин или пароль",
            message_type="error",
            show_link=False
        )


@app.route('/me')
def me():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)