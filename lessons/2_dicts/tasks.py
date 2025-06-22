LESSON_TITLE = "Основы работы со словарями"
LESSON_DESCRIPTION = "Учимся создавать и работать со словарями в Python"

TASKS = {
    "task1": {
        "title": "Профиль исследователя",
        "description": "Создайте словарь researcher с ключами: name, age, expeditions (список из 3 экспедиций)",
        "examples": [
            {"input": "", "output": "{'name': 'Григорий', 'age': 35, 'expeditions': ['Амазонка', 'Тибет', 'Сахара']}"}
        ],
        "tests": [
            {"input": "", "output": "{'name': 'Григорий', 'age': 35, 'expeditions': ['Амазонка', 'Тибет', 'Сахара']}"}
        ],
        "time_limit": 5
    },
    "task2": {
        "title": "Каталог артефактов",
        "description": "Создайте словарь artifacts, где ключи - названия, значения - годы находки (3 артефакта)",
        "examples": [
            {"input": "", "output": "{'статуэтка': 1923, 'монета': 1897, 'ваза': 1854}"}
        ],
        "tests": [
            {"input": "", "output": "{'статуэтка': 1923, 'монета': 1897, 'ваза': 1854}"}
        ],
        "time_limit": 5
    },
    "task3": {
        "title": "Обновление снаряжения",
        "description": "Добавьте в словарь equipment новый ключ 'фонарик' со значением 'LED'",
        "examples": [
            {"input": "", "output": "{'палатка': '4-местная', 'компас': 'электронный', 'фонарик': 'LED'}"}
        ],
        "tests": [
            {"input": "", "output": "{'палатка': '4-местная', 'компас': 'электронный', 'фонарик': 'LED'}"}
        ],
        "time_limit": 5
    },
    "task4": {
        "title": "Расшифровка кода",
        "description": "По словарю code_dict выведите значение по ключу 'treasure_location'",
        "examples": [
            {"input": "", "output": "пещера"}
        ],
        "tests": [
            {"input": "", "output": "пещера", "code_dict": {"treasure_location": "пещера", "key": 1945}},
            {"input": "", "output": "остров", "code_dict": {"treasure_location": "остров", "key": 1945}}
        ],
        "time_limit": 5
    }
}
