from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<float:num>')
def index(num):
    multi = num * 2
    text = f"Ваше число {num}, умноженное на 2: {multi}"
    return render_template('index.html', number=multi, text=text)

@app.route('/circle/<float:r>')
def circle_area(r):
    return render_template('index.html', r=r, pi=3.14)

if __name__ == '__main__':
    app.run(debug=True)


