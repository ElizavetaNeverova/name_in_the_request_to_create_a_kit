import sender_stand_request
import data


# эта функция меняет значения в параметре name
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body


def positive_assert(name):
    # В переменную kit_body сохраняется обновленное тело запроса
    kit_body = get_kit_body(name)
    # В переменную kit_response сохраняется результат запроса на создание набора:
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    # Проверяется, что код ответа равен 201
    assert kit_response.status_code == 201
    # Проверяется, что в ответе есть поле name, и оно совпадает с name в запросе
    assert kit_response.json()["name"] == name


def negative_assert(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 400


def negative_assert_no_name(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400


# Тест 1. Успешное создание набора.
# Параметр name состоит из одного символа
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")


# Тест 2. Успешное создание набора.
# Параметр name состоит из 511 символов
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")


# Тест 3. Ошибка
# Параметр name состоит из 0 символов
def test_create_kit_0_letter_in_name_get_error_response():
    negative_assert("")


# Тест 4. Ошибка
# Параметр name состоит из 512 символов
def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")


# Тест 5. Успешное создание набора.
# Параметр name состоит из английских букв
def test_create_kit_english_letter_in_name_get_success_response():
    positive_assert("QWErty")


# Тест 6. Успешное создание набора.
# Параметр name состоит из русских букв
def test_create_kit_russian_letter_in_name_get_success_response():
    positive_assert("Мария")


# Тест 7. Успешное создание набора.
# Параметр name содержит спецсимволы
def test_create_kit_has_special_symbol_in_name_get_success_response():
    positive_assert("\"№%@\",")


# Тест 8. Успешное создание набора.
# Параметр name содержит пробелы
def test_create_kit_has_space_in_name_get_success_response():
    positive_assert(" Человек и КО ")


# Тест 9. Успешное создание набора.
# Параметр name содержит цифры
def test_create_kit_has_number_in_name_get_success_response():
    positive_assert("123")


# Тест 10. Ошибка
# Параметр name не передан
def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    # Удаление параметра name из запроса
    kit_body.pop("name")
    # Проверка полученного ответа
    negative_assert_no_name(kit_body)


# Тест 11. Ошибка
# Параметр name:число
def test_create_kit_number_type_name_get_error_response():
    negative_assert(123)
