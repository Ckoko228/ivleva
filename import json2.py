import json
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
        user_answer = input(item["question"] + " (Да/Нет): ")
        if user_answer.strip().capitalize() == item["answer"]:
            print("Верно!\n")
            score += 1
        else:
            print(f"Неверно. Правильный ответ: {item['answer']}\n")
    print(f"Ваш результат: {score} из {len(data)}")

if __name__ == "__main__":
    quiz()