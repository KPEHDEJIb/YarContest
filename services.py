import os
import subprocess
import sys
import time
from importlib import import_module


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
