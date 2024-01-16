import random

def get_user_choice():
    user_choice = input("Введите ваш выбор (камень, ножницы, бумага): ").lower()
    while user_choice not in ["камень", "ножницы", "бумага"]:
        print("Неверный выбор. Пожалуйста, введите камень, ножницы или бумага.")
        user_choice = input("Введите ваш выбор: ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(["камень", "ножницы", "бумага"])

def determine_winner(user, computer):
    if user == computer:
        return "Ничья!"
    elif (user == "камень" and computer == "ножницы") or \
         (user == "ножницы" and computer == "бумага") or \
         (user == "бумага" and computer == "камень"):
        return "Вы победили!"
    else:
        return "Компьютер победил!"
user_choice = get_user_choice()
computer_choice = get_computer_choice()

print(f"Ваш выбор: {user_choice}")
print(f"Выбор компьютера: {computer_choice}")

result = determine_winner(user_choice, computer_choice)
print(result)