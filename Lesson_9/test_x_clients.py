from Employee import EmployeeApi
from DataBase import EmployeeSQL
from sqlalchemy.orm import sessionmaker


api = EmployeeApi("https://x-clients-be.onrender.com")
db = EmployeeSQL("postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")

# Проверка получения списка сотрудников компании

def test_get_employee():
    # Шаг 1: создаем компанию
    name = "Газпром"
    descr = "надежный поставщик газа российским и зарубежным потребителям"
    result = api.create_company(name, descr)
    new_id = result["id"]

    # Шаг 2: обращаемся к сотрудникам компании через API
    api_result = api.get_employee(new_id)
    # Шаг 3: обращаемся к сотрудникам компании из БД
    my_params = new_id
    db_result = db.get_employees(my_params)

    # Шаг 4: проверить, что списки равны
    assert len(api_result) == len(db_result)

# Проверка создания сотрудника у конкретной компании


def test_add_new():
    # Шаг 1: создаем компанию
    name = "Газпром"
    descr = "надежный поставщик газа российским и зарубежным потребителям"
    result = api.create_company(name, descr)
    new_id = result["id"]

    # Шаг 2: 1-ое обращение к сотрудникам компании через API
    employee_company = api.get_employee(new_id)
    len_before = len(employee_company)

    # Шаг 3: cоздаем сотрудника
    first_name = "Ксения"
    last_name = "Морогова"
    middle_name = "m_ksemia"
    id_company = int(new_id)
    email = "morogovak@maul.ru"
    url = ""
    phone = "7(951)123-45-67"

    new_employee = api.create_employee(first_name, last_name, middle_name, id_company, email, url, phone)
    id_employee = new_employee["id"]

    # Шаг 4: 2-ое обращение к сотрудникам компании через API
    employee_company = api.get_employee(new_id)
    len_after = len(employee_company)

    db.delete(id_employee)

    # Шаг 5: Проверить, что +1
    assert len_after - len_before == 1

    # Шаг 6: Проверим id нового сотрудника к обащающейся компании:
    for employee in employee_company:
        if employee["id"] == id_employee:
            assert employee["firstName"] == first_name
            assert employee["lastName"] == last_name
            assert employee["middleName"] == middle_name
            assert employee["companyId"] == new_id
            assert employee["phone"] == phone
            assert employee["id"] == id_employee

# Обращаемся к сотруднику по id


# def test_get_one_employee():
    # Шаг 1: создаем компанию
    name = "Газпром"
    descr = "надежный поставщик газа российским и зарубежным потребителям"
    result = api.create_company(name, descr)
    new_id = result["id"]

    # Шаг 2: cоздаем сотрудника
    first_name = 'Ксения'
    last_name = 'Морогова'
    middle_name = 'm_ksenia'
    company_id = new_id
    email = 'morogovak@mail.ru'
    phone = '7(951)123-45-67'

    db.create(first_name, last_name, middle_name, company_id, email, phone)
    max_id = db.get_max_id()

    # Шаг 3: получение сотрудника
    new_employee = api.employee_id(max_id)

    # Шаг 4: удаление
    db.delete(max_id)

    assert new_employee["firstName"] == first_name
    assert new_employee["lastName"] == last_name
    assert new_employee["middleName"] == middle_name
    assert new_employee["companyId"] == new_id
    assert new_employee["phone"] == phone
    assert new_employee["email"] == email
    assert new_employee["id"] == max_id
# Изменить информацию о сотруднике


def test_edit():
    # Шаг 1: создаем компанию
    name = "Газпром"
    descr = "надежный поставщик газа российским и зарубежным потребителям"
    result = api.create_company(name, descr)
    new_id = result["id"]

    # Шаг 2: подготовка
    first_name = 'Ксения'
    last_name = 'Морогова'
    middle_name = 'm_ksenia'
    company_id = new_id
    email = 'hmorogovak@mail.ru'
    phone = '7(951)123-45-67'

    db.create(first_name, last_name, middle_name, company_id, email, phone)
    max_id = db.get_max_id()

    # Шаг 3: меняем email сотрудника:
    new_email = "bawino8111@buzblox.com"
    change_employee = api.employee_change(max_id, last_name, new_email, phone)

    # Шаг 4: удаляем компанию
    db.delete(max_id)

    assert change_employee["id"] == max_id
    assert change_employee["email"] == new_email