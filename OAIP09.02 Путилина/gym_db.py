import json
from datetime import datetime
import uuid


# Cохранениe данных в JSON
def save_data(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load_data(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


clients_db = []
trainings_db = []
equipment_db = []

# Загрузка существующих данных
clients_db = load_data('clients.json')
trainings_db = load_data('trainings.json')
equipment_db = load_data('equipment.json')


# Тестовые данные
def add_test_data():
    # Клиенты
    clients_db.append({
        "_id": str(uuid.uuid4()),
        "name": "Александр Миров",
        "phone": "+79911255567",
        "join_date": datetime.now().isoformat()
    })

    # Тренировки
    trainings_db.append({
        "program_id": "PROG001",
        "name": "Силовой тренинг",
        "duration": "2 месяца",
        "description": "Программа для набора массы"
    })

    # Оборудование
    equipment_db.append({
        "equipment_id": "EQ001",
        "name": "Тренажёр Смита",
        "status": "Доступно",
        "location": "Зона силовых"
    })

    # Сохранение данных
    save_data(clients_db, 'clients.json')
    save_data(trainings_db, 'trainings.json')
    save_data(equipment_db, 'equipment.json')


add_test_data()
