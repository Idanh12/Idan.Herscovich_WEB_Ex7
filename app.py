from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return redirect('/about')

@app.route('/about')
def about_func():
    return redirect(url_for('categories_func'))

@app.route('/categories')
def categories_func():
    return 'Here you will see the categories'


if __name__ == '__main__':
    app.run()
