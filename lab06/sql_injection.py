import sqlite3
import tkinter as tk
from tkinter import messagebox


# ІНІЦІАЛІЗАЦІЯ БАЗИ ДАНИХ
def init_db():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            grade INTEGER
        )
    """)

    cursor.execute("DELETE FROM students")

    students_data = [
        ("Іван Петренко", "ivan@gmail.com", 90),
        ("Марія Коваленко", "maria@gmail.com", 85),
        ("Олег Шевченко", "oleg@gmail.com", 75),
    ]

    cursor.executemany("INSERT INTO students (name, email, grade) VALUES (?, ?, ?)", students_data)

    conn.commit()
    conn.close()


# УРАЗЛИВИЙ ПОШУК
def vulnerable_search():
    keyword = entry_search.get()

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    query = f"SELECT * FROM students WHERE name LIKE '%{keyword}%'"
    print("SQL:", query)

    try:
        cursor.execute(query)
        results = cursor.fetchall()
        show_results(results, "🔴 Уразлива версія")
    except Exception as e:
        messagebox.showerror("Помилка", str(e))

    conn.close()


# ЗАХИЩЕНИЙ ПОШУК
def secure_search():
    keyword = entry_search.get()

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    query = "SELECT * FROM students WHERE name LIKE ?"
    cursor.execute(query, (f"%{keyword}%",))
    results = cursor.fetchall()

    show_results(results, "🟢 Захищена версія")
    conn.close()


# ВІДОБРАЖЕННЯ РЕЗУЛЬТАТІВ
def show_results(results, title):
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f"{title}\n\n")

    if results:
        for row in results:
            result_text.insert(tk.END, f"ID: {row[0]}\nІм'я: {row[1]}\nEmail: {row[2]}\nОцінка: {row[3]}\n\n")
    else:
        result_text.insert(tk.END, "Нічого не знайдено")


# GUI
init_db()

root = tk.Tk()
root.title("Лабораторна №6 — SQL Injection Demo")
root.geometry("600x450")
root.configure(bg="#f5f5f5")

tk.Label(root, text="Система пошуку студентів",
         font=("Arial", 16, "bold"),
         bg="#f5f5f5").pack(pady=10)

frame = tk.Frame(root, bg="#f5f5f5")
frame.pack()

tk.Label(frame, text="Введіть ім'я для пошуку:",
         bg="#f5f5f5").grid(row=0, column=0, padx=5)

entry_search = tk.Entry(frame, width=30)
entry_search.grid(row=0, column=1, padx=5)

tk.Button(root,
          text="🔴 Уразливий пошук",
          bg="#ff4d4d",
          fg="white",
          command=vulnerable_search).pack(pady=5)

tk.Button(root,
          text="🟢 Захищений пошук",
          bg="#4CAF50",
          fg="white",
          command=secure_search).pack(pady=5)

result_text = tk.Text(root, height=15, width=70)
result_text.pack(pady=10)

root.mainloop()
if __name__ == "__main__":
    app.run(debug=True)
