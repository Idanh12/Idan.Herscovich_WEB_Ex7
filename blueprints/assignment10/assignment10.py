from flask import Blueprint, render_template, request, redirect, flash
from interact_with_DB import interact_db

assignment10 = Blueprint('assignment10', __name__,
                         static_folder='static',
                         template_folder='templates')


@assignment10.route('/assignment10', methods=['GET', 'POST'])
def assignment10_func():
    query = 'select * from users;'
    users = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users=users)


@assignment10.route('/insert_user', methods=['POST'])
def insert_user_func():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    password = request.form["password"]
    query = "insert into users(first_name, last_name, password) VALUES ('%s', '%s', '%s');" % (
        first_name, last_name, password)
    interact_db(query=query, query_type='commit')
    flash(f'User {first_name} {last_name} inserted successfully, please note that you have interacted with the DB')
    return redirect('/assignment10')


@assignment10.route('/delete_user', methods=['POST'])
def delete_user_func():
    user_id = request.form['id']
    query = "DELETE FROM users WHere id='%s'" % user_id
    interact_db(query=query, query_type='commit')
    flash(f'User {user_id} deleted successfully, please note that you have interacted with the DB')
    return redirect('/assignment10')

@assignment10.route('/update_user', methods=['POST'])
def update_user_func():
    id = request.form['id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    password = request.form['password']
    query = "select * FROM users WHERE id = '%s';" % id
    query_result = interact_db(query=query, query_type='fetch')
    if len(query_result) > 0:
        query = "UPDATE users SET first_name='%s', last_name='%s', password='%s' WHERE id = '%s';" % (first_name, last_name, password, id)
        interact_db(query=query, query_type='commit')
        flash('user updated successfully, please note that you have interacted with the DB')
        return redirect('/assignment10')
    else:
        flash(f'User {id} does not exist, please note no changes were made to the DB')
        return redirect('/assignment10')