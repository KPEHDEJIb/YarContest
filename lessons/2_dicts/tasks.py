LESSON_TITLE = "Основы работы со словарями"
LESSON_DESCRIPTION = "Учимся создавать, изменять и работать со словарями в Python"

TASKS = {
    "task1": {
        "title": "Учёт животных",
        "description": "Создайте словарь, в котором находятся пары 'животное-количество' по следующему списку:\n"
                       "1) лев - 2\n2) тигр - 3\n3) зебра - 5\n\nВ конце выведите словарь в консоль.",
        "examples": [
            {"input": "", "output": "{'лев': 2, 'тигр': 3, 'зебра': 5}"}
        ],
        "tests": [
            {"input": "", "output": "{'лев': 2, 'тигр': 3, 'зебра': 5}"}
        ],
        "time_limit": 5
    },
    "task2": {
        "title": "Сколько?",
        "description": "В зоопарке есть:\n1) 2 льва\n2) 3 тигра\n3) 4 жирафа\n4) 5 зебр\n\nНа вход программы поступает "
                       "название животного, количество которого нужно вывести в консоль. Если введённого животного нет "
                       "в словаре, то вывести 'Такого животного нет!'.",
        "examples": [
            {"input": "лев", "output": "2"},
            {"input": "бегедил", "output": "Такого животного нет!"}
        ],
        "tests": [
            {"input": "лев", "output": "2"},
            {"input": "бегедил", "output": "Такого животного нет!"},
            {"input": "тигр", "output": "3"},
            {"input": "жираф", "output": "4"},
            {"input": "тунг-тунг-тунг-тунг-тунг-тунг сахур", "output": "Такого животного нет!"},
            {"input": "зебра", "output": "5"}
        ],
        "time_limit": 5
    },
    "task3": {
        "title": "Новый житель зоопарка",
        "description": "В зоопарке есть 2 льва и 3 тигра (это начальные значения в вашем словаре). На вход программы "
                       "поступает наименование животного (не лев и не тигр) и его количество на следующей строке. "
                       "Необходимо добавить в словарь введённые данные.",
        "examples": [
            {"input": "жираф\n4", "output": "{'лев': 2, 'тигр': 3, 'жираф': 4}"}
        ],
        "tests": [
            {"input": "жираф\n4", "output": "{'лев': 2, 'тигр': 3, 'жираф': 4}"},
            {"input": "зебра\n4", "output": "{'лев': 2, 'тигр': 3, 'зебра': 4}"},
            {"input": "крокодил\n2", "output": "{'лев': 2, 'тигр': 3, 'крокодил': 2}"},
            {"input": "фламинго\n9", "output": "{'лев': 2, 'тигр': 3, 'фламинго': 9}"},
            {"input": "игуана\n1", "output": "{'лев': 2, 'тигр': 3, 'игуана': 1}"},
            {"input": "бык\n1", "output": "{'лев': 2, 'тигр': 3, 'бык': 1}"}
        ],
        "time_limit": 5
    },
    "task4": {
        "title": "Переезд животных",
        "description": "В зоопарке есть:\n1) 2 льва\n2) 3 тигра\n3) 4 жирафа\n4) 5 зебр\n\nНа вход программы поступает "
                       "название животного, которое нужно удалить из словаря. Удалите это животное, а затем выведите "
                       "словарь в консоль.",
        "examples": [
            {"input": "тигр", "output": "{'лев': 2, 'жираф': 4, 'зебра': 5}"}
        ],
        "tests": [
            {"input": "тигр", "output": "{'лев': 2, 'жираф': 4, 'зебра': 5}"},
            {"input": "лев", "output": "{'тигр': 3, 'жираф': 4, 'зебра': 5}"},
            {"input": "жираф", "output": "{'лев': 2, 'тигр': 3, 'зебра': 5}"},
            {"input": "зебра", "output": "{'лев': 2, 'тигр': 3, 'жираф': 4}"}
        ],
        "time_limit": 5
    },
    "task5": {
        "title": "*Кого здесь столько?",
        "description": "Внимание, это сложное задание!\n\nНа вход программы поступает число N (больше или равно 1)"
                       " - количество животных в зоопарке. Далее следует 2*N строк: сначала наименование животного, "
                       "а затем его количество. В конце следует число M - количество какого-то животного. Необходимо "
                       "вывести в консоль имя животного, которого в зоопарке M особей\n\nГарантируется, что только "
                       "один вид животного имеет такое количество особей, а также что животное с таким количеством "
                       "особей существует в зоопарке.",
        "examples": [
            {"input": "3\nлев\n2\nтигр\n3\nжираф\n4\n3", "output": "тигр"}
        ],
        "tests": [
            {"input": "3\nлев\n2\nтигр\n3\nжираф\n4\n3", "output": "тигр"},
            {"input": "3\nлев\n2\nтигр\n3\nжираф\n4\n2", "output": "лев"},
            {"input": "3\nлев\n2\nтигр\n3\nжираф\n4\n4", "output": "жираф"},
            {"input": "6\nлев\n2\nлошадь\n6\nигуана\n1\nзебра\n5\nтигр\n3\nжираф\n4\n5", "output": "зебра"},
            {"input": "1\nслон\n1\n1", "output": "слон"},
            {"input": "4\nлеопард\n2\nволк\n6\nмедведь\n3\nлиса\n2\n3", "output": "медведь"}
        ],
        "time_limit": 5
    }
}
