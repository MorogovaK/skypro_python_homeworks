import requests
import json


class Company:
    def __init__(self, url= "https://x-clients-be.onrender.com/"):
        self.url = url

    def create(self, token: str, body: json):
        headers = {'x-client-token': token}
        response = requests.post(
            self.url + '/company', headers=headers, params=body)
        return response.json()

    def last_active_company_id(self):
        active_params = {'active': 'true'}
        responce = requests.get(
            self.url + '/company', params=active_params)
        return responce.json()[-1]['id']


class Employer:
    def __init__(self, url="https://x-clients-be.onrender.com/"):
        self.url = url

    def get_list(self, company_id: int):
        company = {'company': company_id}
        response = requests.get(
            self.url + '/employee', params=company)
        return response.json()

    def add_new(self, token: str, body: json):
        headers = {'x-client-token': token}
        response = requests.post(
            self.url + '/employee', headers=headers, json=body)
        return response.json()

    def get_into(self, employee_id: int):
        response = requests.get(
            self.url + '/employee' + str(employee_id))
        return response

    def change_info(self, token: str, employee_id: int, body: json):
        headers = {'x-client-token': token}
        response = requests.patch(
            self.url + '/employee' + str(employee_id), headers=headers, json=body)
        return response