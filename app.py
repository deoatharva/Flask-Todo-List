from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

app = Flask(__name__)

# Replace with your actual MongoDB Atlas connection string
MONGO_URI = os.environ.get("MONGO_URI") or "mongodb+srv://foxolor295:uRHuVhM4noOVwMWS@cluster0.fkcizpv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client.todo
todos = db.todos

@app.route('/')
def index():
    all_todos = todos.find()
    return render_template('index.html', todos=all_todos)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        todos.insert_one({'task': task})
    return redirect('/')

@app.route('/update/<id>', methods=['POST'])
def update(id):
    updated_task = request.form.get('updated_task')
    todos.update_one({'_id': ObjectId(id)}, {'$set': {'task': updated_task}})
    return redirect('/')

@app.route('/delete/<id>')
def delete(id):
    todos.delete_one({'_id': ObjectId(id)})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
