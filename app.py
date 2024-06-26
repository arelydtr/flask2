from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de tareas (almacenada en memoria para este ejemplo)
tasks = []

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)