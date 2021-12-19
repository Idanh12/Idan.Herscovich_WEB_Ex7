from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def home_page():  # put application's code here
    return render_template('cv.html')


@app.route('/block')
def about_func():
    return render_template('block.html', name_of_class="web", degree='BSc', admin=True, Languages=['hebrew (native)', 'English (fluent)'])


if __name__ == '__main__':
    app.run()
