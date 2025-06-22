from flask import Flask, render_template, request, jsonify
import subprocess
import os
import time
import sys

app = Flask(__name__)

# Конфигурация заданий
TASKS = {
    'task1': {
        'title': 'Hello, World!',
        'description': 'Напишите программу на Python, которая выводит строку "Hello, world!" (без кавычек).',
        'examples': [
            {'input': '', 'output': 'Hello, world!'}
        ],
        'tests': [
            {'input': '', 'output': 'Hello, world!'},
            {'input': 'test', 'output': 'Hello, world!'}  # Проверка, что программа игнорирует ввод
        ],
        'time_limit': 1,
        'memory_limit': 16 * 1024 * 1024,
    },
    'task2': {
        'title': 'Сумма двух чисел',
        'description': 'Напишите программу, которая считывает два числа и выводит их сумму.',
        'examples': [
            {'input': '2\n3', 'output': '5'},
            {'input': '-1\n5', 'output': '4'}
        ],
        'tests': [
            {'input': '2\n3', 'output': '5'},
            {'input': '-1\n5', 'output': '4'},
            {'input': '0\n0', 'output': '0'},
            {'input': '123\n456', 'output': '579'},
            {'input': '-10\n-20', 'output': '-30'}
        ],
        'time_limit': 1,
        'memory_limit': 16 * 1024 * 1024,
    }
}


@app.route('/')
def index():
    return render_template('index.html', tasks=TASKS)


@app.route('/<task_id>')
def task(task_id):
    if task_id not in TASKS:
        return "Задание не найдено", 404

    # Используем task1.html как шаблон для всех задач
    return render_template('task1.html', task=TASKS[task_id])


def run_code(code, input_data, time_limit):
    temp_file = f'temp_{time.time()}.py'
    with open(temp_file, 'w') as f:
        f.write(code)

    result = {
        'output': '',
        'error': '',
        'time': 0,
        'exit_code': 0
    }

    try:
        start_time = time.time()

        # Перенаправляем stdin для передачи входных данных
        process = subprocess.Popen(
            [sys.executable, temp_file],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )

        try:
            stdout, stderr = process.communicate(
                input=input_data,
                timeout=time_limit
            )
            result['time'] = time.time() - start_time
            result['output'] = stdout.strip()
            result['error'] = stderr.strip()
            result['exit_code'] = process.returncode
        except subprocess.TimeoutExpired:
            process.kill()
            result['error'] = 'Time limit exceeded'
    except Exception as e:
        result['error'] = str(e)
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)

    return result


@app.route('/submit/<task_id>', methods=['POST'])
def submit(task_id):
    if task_id not in TASKS:
        return jsonify({'status': 'error', 'message': 'Task not found'}), 404

    code = request.form.get('code', '')
    if not code:
        return jsonify({'status': 'error', 'message': 'Empty code'}), 400

    task = TASKS[task_id]
    test_results = []
    all_passed = True

    for i, test in enumerate(task['tests'], 1):
        test_result = {
            'test_number': i,
            'input': test['input'],
            'expected': test['output'],
            'passed': False,
            'output': '',
            'error': '',
            'time': 0
        }

        run_result = run_code(code, test['input'], task['time_limit'])

        test_result.update({
            'output': run_result['output'],
            'error': run_result['error'],
            'time': run_result['time']
        })

        if run_result['exit_code'] != 0:
            test_result['status'] = 'RE'
            test_result['error'] = run_result['error']
            all_passed = False
        elif run_result['output'] == test['output']:
            test_result['status'] = 'OK'
            test_result['passed'] = True
        else:
            test_result['status'] = 'WA'
            all_passed = False

        test_results.append(test_result)

    return jsonify({
        'status': 'OK' if all_passed else 'WA',
        'test_results': test_results,
        'all_passed': all_passed
    })


if __name__ == '__main__':
    app.run(debug=True)
