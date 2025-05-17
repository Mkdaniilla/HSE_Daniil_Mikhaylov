import json
import csv
import re
from collections import defaultdict

# === 1. Читаем ИНН из traders.txt ===
def read_inn_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip()]

# === 2. Загружаем данные из traders.json ===
def load_traders_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# === 3. Отбираем организации по INN ===
def filter_traders_by_inn(traders_data, inn_list):
    result = []
    for trader in traders_data:
        if trader.get("inn") in inn_list:
            result.append({
                "ИНН": trader.get("inn"),
                "ОГРН": trader.get("ogrn"),
                "адрес": trader.get("address")
            })
    return result

# === 4. Сохраняем результат в traders.csv ===
def save_to_csv(data, file_path):
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["ИНН", "ОГРН", "адрес"])
        writer.writeheader()
        writer.writerows(data)

# === 5. Ищем email-адреса в тексте ===
def extract_emails(text):
    if not isinstance(text, str):
        return []
    pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    return re.findall(pattern, text)

# === 6. Извлекаем email по ИНН из efrsb_messages.json ===
def extract_emails_by_inn(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        messages = json.load(file)

    result = defaultdict(set)

    for msg in messages:
        inn = msg.get("publisher_inn")
        if not inn:
            continue

        for value in msg.values():  # Поиск email во всех полях
            emails = extract_emails(str(value))
            result[inn].update(emails)

    return result

# === 7. Сохраняем результат в emails.json ===
def save_emails_json(email_dict, file_path):
    cleaned = {inn: list(emails) for inn, emails in email_dict.items()}
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(cleaned, f, ensure_ascii=False, indent=2)

# === 8. Главная функция ===
def main():
    # Часть 1 — traders.csv
    inn_list = read_inn_from_txt("traders.txt")
    traders_data = load_traders_json("traders.json")
    filtered = filter_traders_by_inn(traders_data, inn_list)
    save_to_csv(filtered, "traders.csv")

    # Часть 2 — emails.json
    email_dict = extract_emails_by_inn("efrsb_messages.json")
    save_emails_json(email_dict, "emails.json")

# === 9. Запуск ===
if __name__ == "__main__":
    main()
