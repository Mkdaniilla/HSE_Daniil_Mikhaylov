# === Математические функции ===

# 1. Факториал числа
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 2. Поиск наибольшего из трёх чисел (принимает кортеж)
def max_of_three(numbers):
    return max(numbers)


# 3. Площадь прямоугольного треугольника (по двум катетам)
def triangle_area(a, b):
    return 0.5 * a * b


# === Словарь с судами ===

courts = {
    "A40": {
        "name": "Арбитражный суд города Москвы",
        "address": "115225, г. Москва, ул. Б. Тульская, 17"
    },
    "A56": {
        "name": "Арбитражный суд СПб и Ленинградской области",
        "address": "191015, г. Санкт-Петербург, Суворовский проспект, д. 50/52"
    },
    "A75": {
        "name": "Арбитражный суд Челябинской области",
        "address": "454000, г. Челябинск, ул. Воровского, 2"
    }
}


# === Функция генерации шапки для процессуального документа ===

def generate_header(defendant: dict, case_number: str) -> str:
    court_code = case_number.split('-')[0]  # Пример: A40 из A40-123456/2023
    court = courts.get(court_code, {
        "name": "Суд не найден",
        "address": "адрес отсутствует"
    })

    # 🔁 ДАННЫЕ ИСТЦА — подставь свои реальные данные!
    plaintiff = {
        "name": "Пупкин Василий Геннадьевич",
        "inn": "1236182357",
        "ogrnip": "218431927812733",
        "address": "123534, г. Москва, ул. Водников, 13"
    }

    return f"""
{court['name']}
Адрес: {court['address']}

Истец: {plaintiff['name']}
ИНН {plaintiff['inn']} ОГРНИП {plaintiff['ogrnip']}
Адрес: {plaintiff['address']}

Ответчик: {defendant['name']}
ИНН {defendant['inn']} ОГРН {defendant['ogrn']}
Адрес: {defendant['address']}

Номер дела {case_number}
""".strip()


# === Функция генерации шапок для списка ответчиков ===

def generate_headers_for_list(defendants: list):
    for defendant in defendants:
        print(generate_header(defendant, defendant["case_number"]))
        print("\n" + "-" * 60 + "\n")


# === Пример использования ===

if __name__ == "__main__":
    # Математика:
    print("Факториал 5:", factorial(5))
    print("Максимум из (3, 7, 1):", max_of_three((3, 7, 1)))
    print("Площадь треугольника 3 и 4:", triangle_area(3, 4))

    # Ответчики:
    respondents = [
        {
            "name": 'ООО "Кооператив Озеро"',
            "inn": "1231231231",
            "ogrn": "123124129312941",
            "address": "123534, г. Москва, ул. Красивых молдавских партизан, 69",
            "case_number": "A40-123456/2023"
        },
        {
            "name": 'ООО "Ромашка"',
            "inn": "9876543210",
            "ogrn": "1111111111111",
            "address": "456000, г. СПб, ул. Ленина, 5",
            "case_number": "A56-987654/2023"
        }
    ]

    generate_headers_for_list(respondents)
