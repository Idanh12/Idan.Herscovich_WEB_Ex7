from flask import Flask, redirect, url_for, render_template, request, session
from list import users

app = Flask(__name__)

app.secret_key = "abc"

@app.route('/')
def home_page():  # put application's code here
    return render_template('cv.html')


@app.route('/block')
def about_func():
    return render_template('block.html', name_of_class="web", degree='BSc', admin=True,
                           Languages=['Hebrew (native)', 'English (fluent)'])


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9_func():
    if request.method == 'GET':
        if "Search" in request.args:
            search = request.args["Search"]
            res = []
            for user in users:
                if user["first name"] == search or user["Last name"] == search:
                    res.append(user)
            if search == "":
                res = users
            if session.get('login'):
                return render_template('assignment9.html',
                                       res=res,
                                       nickname=session.get('nick_name'))
            else:
                return render_template('assignment9.html', res=res)
    if request.method == 'POST':
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        nick_name = request.form["nick_name"]
        email = request.form["email"]
        session['nick_name'] = nick_name
        session['login'] = True
    if session.get('login'):
        return render_template('assignment9.html',
                               nickname=session.get('nick_name'))
    return render_template('assignment9.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout_func():
    session.clear()
    return render_template('assignment9.html')


if __name__ == '__main__':
    app.run(debug=True)
