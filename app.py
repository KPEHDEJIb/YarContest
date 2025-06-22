from flask import Flask, render_template, request, jsonify
import subprocess
import os
import time
import sys

app = Flask(__name__)

# Конфигурация задания
TASKS = {
    'task1': {
        'title': 'Hello, World!',
        'description': 'Напишите программу на Python, которая выводит строку "Hello, world!" (без кавычек).',
        'examples': [
            {'input': '', 'output': 'Hello, world!'}
        ],
        'time_limit': 1,  # 1 секунда
        'memory_limit': 16 * 1024 * 1024,  # 16 MB
    }
}


@app.route('/')
def index():
    return render_template('index.html', tasks=TASKS)


@app.route('/<task_id>')
def task(task_id):
    if task_id not in TASKS:
        return "Задание не найдено", 404
    return render_template('task1.html', task=TASKS[task_id])


@app.route('/submit/<task_id>', methods=['POST'])
def submit(task_id):
    if task_id not in TASKS:
        return jsonify({'status': 'error', 'message': 'Task not found'}), 404

    code = request.form.get('code', '')
    if not code:
        return jsonify({'status': 'error', 'message': 'Empty code'}), 400

    # Создаем временный файл для кода
    temp_file = f'temp_{time.time()}.py'
    with open(temp_file, 'w') as f:
        f.write(code)

    result = {
        'status': 'OK',
        'output': '',
        'expected': 'Hello, world!',
        'error': '',
        'time': 0,
        'memory': 0
    }

    try:
        start_time = time.time()

        # Запускаем программу с ограничениями
        process = subprocess.Popen(
            [sys.executable, temp_file],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )

        try:
            stdout, stderr = process.communicate(timeout=TASKS[task_id]['time_limit'])
            result['time'] = time.time() - start_time

            if process.returncode != 0:
                result['status'] = 'RE'
                result['error'] = stderr
            else:
                output = stdout.strip()
                result['output'] = output
                if output != result['expected']:
                    result['status'] = 'WA'
        except subprocess.TimeoutExpired:
            process.kill()
            result['status'] = 'TL'
            result['error'] = 'Time limit exceeded'
    except Exception as e:
        result['status'] = 'CE'
        result['error'] = str(e)
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
