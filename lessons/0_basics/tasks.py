LESSON_TITLE = "Основы Python"
LESSON_DESCRIPTION = "Начальные задания для изучения Python"

TASKS = {
    'hello': {
        'title': 'Hello World',
        'description': 'Напишите программу, которая выводит "Hello, world!"',
        'examples': [{'input': '', 'output': 'Hello, world!'}],
        'tests': [
            {'input': '', 'output': 'Hello, world!'},
            {'input': '123', 'output': 'Hello, world!'}
        ],
        'time_limit': 1,
        'memory_limit': 16 * 1024 * 1024
    },
    'sum': {
        'title': 'Сумма чисел',
        'description': 'Напишите программу, которая складывает два числа',
        'examples': [
            {'input': '2\n3', 'output': '5'},
            {'input': '-1\n5', 'output': '4'}
        ],
        'tests': [
            {'input': '2\n3', 'output': '5'},
            {'input': '0\n0', 'output': '0'}
        ],
        'time_limit': 1,
        'memory_limit': 16 * 1024 * 1024
    }
}
