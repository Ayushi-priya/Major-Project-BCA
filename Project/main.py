from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, current_user
from project.models import Todo
from project.auth import *
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    id = current_user.id
    if request.method=='POST':
        title= request.form['title']
        desc= request.form['desc']

        user = current_user.id

        todo=Todo(title=title,desc=desc,user_id=user)
        db.session.add(todo)
        db.session.commit()

    allTodo=current_user.todos
    return render_template('home.html', name=current_user.name, allTodo=allTodo)

@main.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method=='POST':
        title= request.form['title']
        desc= request.form['desc']
        todo=Todo.query.filter_by(id=id).first()
        todo.title=title
        todo.desc=desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/home")
    todo=Todo.query.filter_by(id=id).first()
    return render_template('update.html', name=current_user.name, todo=todo)

@main.route('/delete/<int:id>')
def delete(id):
    todo=Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/home")