from flask import Flask, render_template, request, jsonify
from importlib import import_module
import subprocess
import time
import sys
import os

app = Flask(__name__)


# Автоматическая загрузка уроков
def load_lessons():
    lessons = {}
    lessons_dir = os.path.join(os.path.dirname(__file__), 'lessons')

    for lesson_name in os.listdir(lessons_dir):
        lesson_path = os.path.join(lessons_dir, lesson_name)
        if os.path.isdir(lesson_path) and lesson_name != '__pycache__':
            try:
                lesson_module = import_module(f'lessons.{lesson_name}.tasks')
                lessons[lesson_name] = {
                    'title': getattr(lesson_module, 'LESSON_TITLE', lesson_name),
                    'description': getattr(lesson_module, 'LESSON_DESCRIPTION', ''),
                    'tasks': getattr(lesson_module, 'TASKS', {})
                }
            except ImportError as e:
                print(f"Error loading lesson {lesson_name}: {e}")
    return lessons


LESSONS = load_lessons()


@app.route('/')
def index():
    return render_template('index.html', lessons=LESSONS)


@app.route('/lesson/<lesson_name>/<task_name>')
def show_task(lesson_name, task_name):
    if lesson_name not in LESSONS:
        return "Урок не найден", 404

    lesson = LESSONS[lesson_name]

    if task_name not in lesson['tasks']:
        return "Задание не найдено", 404

    task = lesson['tasks'][task_name]

    return render_template('lesson.html',
                           lesson=lesson,
                           current_task=task,
                           lesson_name=lesson_name,
                           task_name=task_name)


def run_code(code, input_data, time_limit):
    """Запуск кода с ограничениями"""
    temp_file = f'temp_{time.time()}.py'

    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(code)

    result = {
        'output': '',
        'error': '',
        'time': 0,
        'exit_code': 0
    }

    try:
        start_time = time.time()
        process = subprocess.Popen(
            [sys.executable, temp_file],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            encoding='utf-8'
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


@app.route('/submit/<lesson_name>/<task_name>', methods=['POST'])
def submit(lesson_name, task_name):
    # Проверяем существование урока и задачи
    if lesson_name not in LESSONS:
        return jsonify({'status': 'error', 'message': 'Lesson not found'}), 404

    if task_name not in LESSONS[lesson_name]['tasks']:
        return jsonify({'status': 'error', 'message': 'Task not found'}), 404

    # Получаем код из формы
    code = request.form.get('code', '')
    if not code:
        return jsonify({'status': 'error', 'message': 'Empty code'}), 400

    task = LESSONS[lesson_name]['tasks'][task_name]
    test_results = []
    all_passed = True

    # Запускаем все тесты для задачи
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
            test_result['status'] = 'RE'  # Runtime Error
            test_result['error'] = run_result['error']
            all_passed = False
        elif run_result['output'] == test['output']:
            test_result['status'] = 'OK'
            test_result['passed'] = True
        else:
            test_result['status'] = 'WA'  # Wrong Answer
            all_passed = False

        test_results.append(test_result)

    return jsonify({
        'status': 'OK' if all_passed else 'WA',
        'test_results': test_results,
        'all_passed': all_passed
    })


if __name__ == '__main__':
    app.run(debug=True)