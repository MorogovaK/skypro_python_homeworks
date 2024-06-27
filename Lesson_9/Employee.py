import requests


class EmployeeApi:
    #  Инициализация

    def __init__(self, url):
        self.url = url

    # Получить токен авторизации

    def get_token(self, user='flora', password='nature-fairy'):
        creds = {
            "username": user,
            "password": password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]

# Добавить компанию:

    def create_company(self, name, description=""):
        company = {
            "name": name,
            "description": description
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/company',json=company, headers=my_headers)
        return resp.json()

    # Получить список сотрудников

    def get_employee(self, id):
        resp = requests.get(self.url + '/employee?company=' + str(id))
        return resp.json()

    # Добавить сотрудника:
    def create_employee(self, first_name, last_name, middle_name, id_company, email, url, phone):
        employee = {
        "firstName": first_name,
        "lastName": last_name,
        "middleName": middle_name,
        "companyId": id_company,
        "email": email,
        "url": url,
        "phone": phone
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/employee',json=employee, headers=my_headers)
        return resp.json()

    # Получить сотрудника по id

    def employee_id(self, id):
        resp = requests.get(self.url + '/employee/' + str(id))
        return resp.json()

    # Изменить информацию о сотруднике

    def employee_change(self, id, last_name="", email="", url="", phone=""):
        employee = {
            "lastName": last_name,
            "email": email,
            "url": url,
            "phone": phone
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.patch(self.url + '/employee/' + str(id),json=employee, headers=my_headers)
        return resp.json()