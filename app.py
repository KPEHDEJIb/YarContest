from flask import Flask, render_template, request, jsonify
from services import run_code, LESSONS

app = Flask(__name__)



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