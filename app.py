from flask import Flask, redirect, url_for, render_template, request, session, jsonify
from list import users
from interact_with_DB import *
import requests

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


# assignment10
from blueprints.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)

# assignment11
@app.route('/assignment11/users', methods=['GET', 'POST'])
def assignment11_users_func():
    query = 'select * from users;'
    users = interact_db(query=query, query_type='fetch')
    response = jsonify(users)
    return response


@app.route('/assignment11')
def assignment11_init_func():  # put application's code here
    return render_template('assignment11.html')


@app.route('/assignment11/outer_source', methods=['GET', 'POST'])
def assignment11_outer_source():
    return render_template('assignment11.html')


@app.route('/get_user', methods=['POST'])
def assignment11_get_user():
    id = request.form['id']
    return render_template('assignment11.html', id=id)


@app.route('/req_backend')
def req_backend_func():
    user=None
    if "user" in request.args and request.args['user']!='':
        user = request.args['user']
    res = requests.get(f'https://reqres.in/api/users/{user}')
    res = res.json()
    return render_template('assignment11.html', user=res)


#Assignment 12:
@app.route('/assignment12/restapi_users/<int:user_id>')
@app.route('/assignment12/restapi_users', defaults={'user_id': 1})
def json_user_by_id(user_id):
    query = 'select * from users where id=%s' % user_id
    users = interact_db(query=query, query_type='fetch')
    if len(users) == 0:
        dict_to_print = {
            'status': 'failed',
            'message': 'user not found'
        }
    else:
        dict_to_print = {
            f'id': users[0].id,
            'first name': users[0].first_name,
            'last name': users[0].last_name,
        }
    return jsonify(dict_to_print)

if __name__ == '__main__':
    app.run(debug=True)
