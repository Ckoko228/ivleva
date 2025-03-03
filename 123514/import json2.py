import random

data = [
    {"question": "Является ли JSON языком программирования?", "answer": "Нет"},
    {"question": "Может ли JSON содержать комментарии?", "answer": "Нет"},
    {"question": "Является ли JSON подмножеством JavaScript?", "answer": "Да"},
    {"question": "Могут ли ключи в JSON быть числами?", "answer": "Нет"},
    {"question": "Поддерживает ли JSON массивы?", "answer": "Да"},
    {"question": "Может ли JSON представлять объекты?", "answer": "Да"},
    {"question": "Использует ли JSON строгую типизацию?", "answer": "Нет"},
    {"question": "Является ли JSON текстовым форматом обмена данными?", "answer": "Да"},
    {"question": "Поддерживает ли JSON булевые значения?", "answer": "Да"},
    {"question": "Можно ли хранить функции в JSON?", "answer": "Нет"}
]

def quiz():
    score = 0
    random.shuffle(data)
    for item in data:
        if input(item["question"] + " (Да/Нет): ").strip().capitalize() == item["answer"]:
            score += 1
    print(f"Ваш результат: {score} из {len(data)}")

if __name__ == "__main__":
    quiz()
