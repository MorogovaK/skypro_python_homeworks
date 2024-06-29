from EmployeeAPI import EmployeeApi
from EmployeeSQL import EmployeeSQL
import allure

api = EmployeeApi("https://x-clients-be.onrender.com")
db = EmployeeSQL("postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")

# Проверка получения списка сотрудников компании


@allure.title("Создание организации")
@allure.description("Проверка, что созданная компания отображается в списке")
@allure.feature("CREATE")
@allure.severity("blocker")
def test_get_employee():
    with allure.step("создаем компанию"):
        name = "Газпром"
        descr = "надежный поставщик газа российским и зарубежным потребителям"
        result = api.create_company(name, descr)
        new_id = result["id"]

    with allure.step("обращаемся к сотрудникам компании через API"):
        api_result = api.get_employee(str(new_id))
    with allure.step("обращаемся к сотрудникам компании из БД"):
        my_params = new_id
        db_result = db.get_employees(my_params)

    with allure.step("проверить, что списки равны"):
        assert len(api_result) == len(db_result)


@allure.title("Создание организации")
@allure.description("Проверка создания сотрудника у конкретной компании")
@allure.feature("CREATE")
@allure.severity("blocker")
def test_add_new():
    with allure.step("создаем компанию"):
        name = "Газпром"
        descr = "надежный поставщик газа российским и зарубежным потребителям"
        result = api.create_company(name, descr)
        new_id = result["id"]

    with allure.step("1-ое обращение к сотрудникам компании через API"):
        employee_company = api.get_employee(str(new_id))
        len_before = len(employee_company)

    with allure.step("cоздаем сотрудника"):
        first_name = "Ксения"
        last_name = "Морогова"
        middle_name = "m_ksemia"
        id_company = new_id
        email = "morogovak@maul.ru"
        url = ""
        phone = "7(951)123-45-67"

        new_employee = api.create_employee(first_name, last_name, middle_name, id_company, email, url, phone)
        id_employee = new_employee["id"]

    with allure.step("2-ое обращение к сотрудникам компании через API"):
        employee_company = api.get_employee(str(new_id))
        len_after = len(employee_company)

        db.delete(id_employee)

    with allure.step("Проверить, что +1"):
        assert len_after - len_before == 1


    with allure.step("Проверим id нового сотрудника к обащающейся компании:"):
        for employee in employee_company:
            if employee["id"] == id_employee:
                assert employee["firstName"] == first_name
                assert employee["lastName"] == last_name
                assert employee["middleName"] == middle_name
                assert employee["companyId"] == new_id
                assert employee["phone"] == phone
                assert employee["id"] == id_employee


@allure.title("Обращаемся к сотруднику по id")
@allure.description("Проверка данных у сотрудника по id")
@allure.feature("READ")
@allure.severity("blocker")
def test_get_one_employee():
    connection_string = "postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx"
    db = EmployeeSQL(connection_string)
    with allure.step("создаем компанию"):
        name = "Газпром"
        descr = "надежный поставщик газа российским и зарубежным потребителям"
        result = api.create_company(name, descr)
        new_id = result["id"]

    with allure.step("cоздаем сотрудника"):
        first_name = "Ксения"
        last_name = "Морогова"
        middle_name = "m_ksemia"
        company_id = new_id
        email = "morogovak@maul.ru"
        phone = "7(951)123-45-67"

        db.create(first_name, last_name, middle_name, company_id, email, phone)
        max_id = db.get_max_id()

    with allure.step("получение сотрудника"):
        new_employee = api.employee_id(str(max_id))

    with allure.step("удаление"):
        db.delete(str(max_id))

    assert new_employee["firstName"] == first_name
    assert new_employee["lastName"] == last_name
    assert new_employee["middleName"] == middle_name
    assert new_employee["companyId"] == new_id
    assert new_employee["phone"] == phone
    assert new_employee["email"] == email
    assert new_employee["id"] == max_id


@allure.title("Изменить информацию о сотрудникеи")
@allure.description("Проверка измененных данных у сотрудника")
@allure.feature("UPDATE")
@allure.severity("blocker")
def test_edit():
    with allure.step("создаем компанию"):
        name = "Газпром 2"
        descr = "надежный поставщик газа российским и зарубежным потребителям"
        result = api.create_company(name, descr)
        new_id = result["id"]

    with allure.step("создаем сотрудника"):
        first_name = "Ксения"
        last_name = "Морогова"
        middle_name = "m_ksemia"
        company_id = new_id
        email = "morogovak@maul.ru"
        phone = "7(951)123-45-67"

        db.create(first_name, last_name, middle_name, company_id, email, phone)
        max_id = db.get_max_id()

    with allure.step("меняем email сотрудника"):
        new_email = "morogovaK1203@mail.com"
        change_employee = api.employee_change(max_id, last_name, new_email, phone)

    with allure.step("удаляем сотрудника"):
        db.delete(str(max_id))

    with allure.step("проверить id сотрудника"):
        assert change_employee["id"] == max_id

    with allure.step("проверить измененный email"):
        assert change_employee["email"] == new_email