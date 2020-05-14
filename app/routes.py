from flask import jsonify, request

from app import app, db
from app.models import Task, Post

@app.route('/api/tasks', methods=['GET', 'POST'])
def task_list():
    if request.method == 'POST':
        data = request.json
        task = Task(title=data.get('title'))
        db.session.add(task)
        db.session.commit()
    tasks = Task.query.all()
    tasks = [t.serialize() for t in tasks]
    return jsonify(tasks)

@app.route('/api/tasks/<id>', methods=['GET', 'PUT', 'DELETE'])
def task_detail(id):
    task = Task.query.get(id)
    if request.method == 'PUT':
        data = request.json
        task.title = data.get('title', task.title)
        task.is_completed = data.get('is_completed', task.is_completed)
        db.session.commit()
    if request.method == 'DELETE':
        db.session.delete(task)
        db.session.commit()
    return jsonify(task.serialize())

@app.route('/api/posts')
def posts_list():
    posts = Post.query.all()
    posts = [p.serialize() for p in posts]
    return jsonify(posts)