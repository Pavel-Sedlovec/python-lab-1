import importlib
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
rare_dir = os.path.abspath(os.path.join(current_dir, '..', 'rare'))
sys.path.append(rare_dir)

def run_all_tasks():
    
    tasks = [
        "00_distance", "01_circle", "02_operations", "03_favorite_movies",
        "04_my_family", "05_zoo", "06_songs_list", "07_secret",
        "08_garden", "09_shopping", "10_store"
    ]
    
    for task in tasks:
        print(f"\nЗадача {task}.py")
        try:
            module = importlib.import_module(task)
            module.run()
        except ModuleNotFoundError:
            print(f"Ошибка: файл {task}.py не найден в папке {rare_dir}")

if __name__ == '__main__':
    run_all_tasks()