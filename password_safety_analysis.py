import re

def analyze_password(password, name, birth_date):
    recommendations = []
    score = 10

    # Розділяємо дату народження
    day, month, year_full = birth_date.split('.')
    date_parts = (day, month, year_full)

    # Перевіряємо, чи міститься ім’я або дата народження у паролі
    name_in_password = name.lower() in password.lower()
    date_in_password = any(part in password for part in date_parts)

    # Перевірка довжини
    if len(password) < 8:
        score -= 3
        recommendations.append("Пароль занадто короткий (мінімум 8 символів).")

    # Велика літера
    if not any(c.isupper() for c in password):
        score -= 1
        recommendations.append("Додайте хоча б одну велику літеру.")

    # Мала літера
    if not any(c.islower() for c in password):
        score -= 1
        recommendations.append("Додайте хоча б одну малу літеру.")

    # Цифра
    if not any(c.isdigit() for c in password):
        score -= 1
        recommendations.append("Додайте хоча б одну цифру.")

    # Спеціальні символи
    if not any(not c.isalnum() for c in password):
        score -= 2
        recommendations.append("Додайте спеціальний символ (наприклад !, @, #, $, %).")

    # Ім’я у паролі
    if name_in_password:
        score -= 2
        recommendations.append("Не використовуйте власне ім’я у паролі.")

    # Дата народження у паролі
    if date_in_password:
        score -= 1
        recommendations.append("Не використовуйте дату народження або її частину у паролі.")

    # Мінімальна оцінка
    score = max(1, score)

    # Результати
    print("\nРЕЗУЛЬТАТ АНАЛІЗУ")
    print(f"Оцінка безпеки пароля: {score}/10")

    if score >= 8:
        print("Рівень безпеки: Високий ✅")
    elif score >= 5:
        print("Рівень безпеки: Середній ⚠️")
    else:
        print("Рівень безпеки: Низький ❌")

    # Рекомендації
    if recommendations:
        print("\nРекомендації для покращення:")
        for r in recommendations:
            print("-", r)
    else:
        print("\nПароль відповідає всім вимогам безпеки!")


# Функція для перевірки правильності формату дати
def input_birth_date():
    while True:
        birth_date = input("Введіть дату народження (у форматі DD.MM.YYYY): ")
        if re.match(r"^\d{2}\.\d{2}\.\d{4}$", birth_date):
            day, month, year = birth_date.split('.')
            if 1 <= int(day) <= 31 and 1 <= int(month) <= 12:
                return birth_date
            else:
                print("Некоректна дата. Спробуйте ще раз.")
        else:
            print("Невірний формат! Використовуйте формат DD.MM.YYYY.")


# Основна логіка програми
while True:
    print("\nВАС ВІТАЄ АНАЛІЗ БЕЗПЕКИ ПАРОЛЯ!")
    name = input("Введіть ваше ім’я: ")
    birth_date = input_birth_date()
    password = input("Введіть пароль для перевірки: ")

    analyze_password(password, name, birth_date)

    # Вибір користувача
    choice = input("\nЗакінчити сесію? (y - так, n - продовжити): ").lower()

    if choice == 'y':
        print("\nСесію завершено. Дякуємо за використання програми! 👋")
        break
    elif choice == 'n':
        print("\nБули раді вам допомогти! Щоб почати сесію знову, натисніть команду y 💡")
        # Очікуємо підтвердження від користувача
        while True:
            restart = input("\nПочати сесію знову? (y - так): ").lower()
            if restart == 'y':
                print("\nЗапускаємо нову сесію...")
                break
            else:
                print("Для повторного запуску натисніть лише 'y'.")
