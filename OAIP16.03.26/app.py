from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'simple-key-for-practice'

materials = [
    {
        "id": 1,
        "title": "Flask для ботов",
        "category": "Книга",
        "author": "Настя",
        "description": "Введение во Flask для чайников"
    },
    {
        "id": 2,
        "title": "Python",
        "category": "Книга",
        "author": "Анастасия",
        "description": "Основы программирования на Python"
    },
    {
        "id": 3,
        "title": "HTML и CSS",
        "category": "Видеокурс",
        "author": "НаСтЯ",
        "description": "Основы верстки сайтов"
    }
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/materials')
def materials_list():
    total = len(materials)
    categories = {}

    for item in materials:
        cat = item['category']
        if cat in categories:
            categories[cat] += 1
        else:
            categories[cat] = 1

    return render_template('materials_list.html',
                           materials=materials,
                           total=total,
                           categories=categories)


@app.route('/materials/<int:material_id>')
def material_detail(material_id):
    for item in materials:
        if item['id'] == material_id:
            return render_template('material_detail.html', material=item)
    return "Материал не найден", 404


@app.route('/add', methods=['GET', 'POST'])
def add_material():
    if not session.get('logged_in'):
        return redirect('/login')

    if request.method == 'POST':
        title = request.form['title']
        category = request.form['category']
        author = request.form['author']
        description = request.form['description']

        new_material = {
            'id': len(materials) + 1,
            'title': title,
            'category': category,
            'author': author,
            'description': description
        }

        materials.append(new_material)

        return redirect('/materials')

    return render_template('add_material.html')


@app.route('/add-book', methods=['GET', 'POST'])
def add_book():
    if not session.get('logged_in'):
        return redirect('/login')

    if request.method == 'POST':
        new_material = {
            'id': len(materials) + 1,
            'title': request.form['title'],
            'category': 'Книга',
            'author': request.form['author'],
            'description': request.form['description']
        }
        materials.append(new_material)
        return redirect('/materials')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == '123':
            session['logged_in'] = True
            session['username'] = username
            return redirect('/add')
        else:
            return render_template('login.html', error='Неверный логин или пароль')

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)