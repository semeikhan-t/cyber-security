import os
import subprocess
import sys
import webbrowser

def main():
    manage_py_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'shield', 'manage.py')
    requirements_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'shield', 'requirements.txt')

    if not os.path.exists(manage_py_path):
        print(f"Файл manage.py не найден по пути {manage_py_path}")
        sys.exit(1)

    if not os.path.exists(requirements_path):
        print(f"Файл requirements.txt не найден по пути {requirements_path}")
        sys.exit(1)

    # Установка пакетов из файла requirements.txt
    subprocess.call([sys.executable, '-m', 'pip', 'install', '-r', requirements_path])

    # Запуск сервера Django
    subprocess.Popen([sys.executable, manage_py_path, 'runserver'])

    # Открытие веб-браузера по адресу http://127.0.0.1:8000/
    webbrowser.open('http://127.0.0.1:8000/')

if __name__ == "__main__":
    main()
