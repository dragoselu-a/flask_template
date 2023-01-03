from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    first_name='John'
    stuff = 'Welcome to the <strong>jungle</strong>'
    book_list = [1984, 'The Martian', 'Ivanhoe']
    return render_template('index.html',
                        first_name = first_name,
                        stuff = stuff,
                        book_list = book_list)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500




if __name__ == "__main__":
    app.run(debug=True)