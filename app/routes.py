# app/routes.py

from flask import jsonify, request
from app import app

tasks = [
  {"id":1, "title": "Task 1", "completed": False},
  {"id": 2, "title": "Task 2", "completed": True},
]
@app.route('/api/v1/tasks', methods=['GET'])
def get_tasks():
  return jsonify({'tasks':tasks})

@app.route('/api/v1/tasks/<int:task_id>' methods=['GET'])
def get_task(task_id):
  tasks = next(( t for t in tasks if t['id'] == task_id),None)
  if task is None:
    return jsonify({'error': 'Task not found'}), 404
  return jsonify({'task': task})

@app.route('/api/v1/tasks', methods=['POST'})
def create_task():
  data = request.get_json()
  new_task = {'id': len(tasks) + 1, 'title': data['title'], 'completed': False}
  tasks.append(new_task)
  return jsonify({'task': new_task}), 201
